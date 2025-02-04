from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import user_passes_test

from .models import Movie
from user_library.models import Like
from .services import add_movies_from_tmdb
from api_services.TMDB.fetch_movies import fetch_popular_movies


def admin_check(user):
    return user.is_superuser  # or user.is_staff for staff users


def list_movie(request):
    '''retrieve the movies from newer to older and display them in the template
    page's goal is to display up to 24 content pieces per page
    '''
    try:
        if Movie:
            # movies = Movie.objects.all()[:24] # will implement a 24 content per page
            movies = Movie.objects.order_by('-id')[:24]
            
            # Get the user's like content
            user_liked_movies = []
            user_liked_movies = Like.objects.filter(
                                            user=request.user.id,
                                            content_type='movie'
                                            ).values_list('object_id', flat=True)

            context = {
                'movies': movies,
                'user_liked_movies': user_liked_movies
                }

            return render(request, 'movie/list_movie.html', context=context)
            
        else:
            return f'No movies found in the database'
    except Exception as e:
        messages.error(request, "the page seems to experience some issue, please try again later")
        print(f" error :{e}")


def movie_overview(request, pk):
    ''' get the movie object from the database using the movie_id parameter in the URL request.
        will pass on with the necessary information such as 'Like' 
    '''
    try:
        if Movie:
        # retrieve the specified movie requested by user
            movie = Movie.objects.get(id=pk)

            # Check if user's like the movie
            user_liked_movie = False
            user_liked_movie = Like.objects.filter(
                                            user=request.user.id,
                                            content_type='movie',
                                            object_id=movie.pk
                                            ).values_list('object_id', flat=True)

            print(f"user_liked :{user_liked_movie}") # debug print

            context = {
                'movie': movie,
                'user_liked_movie': user_liked_movie,
                }
            
            return render(request,'movie/detail_movie.html', context=context)
        
        else:
            return f'No movies found in the database'
        
    except Exception as e:
        messages.error(request, "the page seem to experience some issue, please try again later")
        print(f" error :{e}")


# @user_passes_test(admin_check, login_url="user:login", redirect_field_name="main/home")
def import_movie(request, tmdb_id):
    '''Import a movie in making a request to TMDB api and store it in the database'''
    print(f"request importing a new movie")
    try:
        if request.method == 'GET' and request.user.is_superuser:
            result = add_movies_from_tmdb(tmdb_id)

            # Determine appropriate HTTP status code
            status_code = {
                'added': 201,
                'exists': 200,
                'error': 404
            }.get(result['status'], 400)

            return JsonResponse(result, status=status_code)

        else:
            print(f"Unauthorized access to 'import_movie' page.")
            messages.error(request, "You are not authorized to import movies")
            return redirect('main:home')
        
    except Exception as e:
        messages.error(request, "the page seem to experience some issue, please try again later")
        print(f" error :{e}")





# @user_passes_test(admin_check, login_url="user:login", redirect_field_name="main/home")
def bulk_import_movies(request):
    """
    Bulk import strategy:
    1. Fetch popular movies
    3. Check if already in database / if so, pass.
    3.  loop through each movie to query their data 
    4. Import new movies 
    """
    try:
        if request.user.is_superuser:
            
            page = 1
            while True:
                print(f"request importing bulk new movies") # debug print
                popular_movies = fetch_popular_movies(page)

                if not popular_movies:
                    print(f" The query could not fetch a list of popular movies, check the url.")  # debug print
                    return JsonResponse({'message': 'Bulk import failed, check Url'}, status=404)
                
                for movie in popular_movies['results']:
                    tmdb_id = movie['id']
                    print(f" passing tmdb_id: {tmdb_id}") # debug print

                    # Check if movie exists
                    if not Movie.objects.filter(tmdb_id=tmdb_id).exists():
                        try:
                            add_movies_from_tmdb(tmdb_id)
                            print(f"Imported movie: {movie['title']}")  # not sure it is imported if already exist
                        except Exception as e:
                            print(f"Error importing {movie['title']}: {e}")

                # Break if no more pages
                if page > 1: # will run 2 pages
                    break
                page += 1
            print(f"Imported list popular movies done! success")
            return JsonResponse({'message': 'Bulk import successful'}, status=200)
        
    except Exception as e:
        messages.error(request, "the page seem to experience some issue, please try again later")
        print(f" error :{e}")