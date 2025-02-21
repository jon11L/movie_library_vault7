import requests
from django.core.management.base import BaseCommand

from movie.models import Movie
from serie.models import Serie
from import_data.api_services.TMDB.fetch_movies import fetch_popular_movies
from import_data.api_services.TMDB.fetch_series import fetch_popular_series
from import_data.services import add_movies_from_tmdb, add_series_from_tmdb

import time

class Command(BaseCommand):
    help = 'Import movie and series data from TMDB'

    def handle(self, *args, **kwargs):
        self.import_movies()
        self.import_series()

    def import_movies(self):
        """
        Bulk import strategy:
        1. Fetch popular list of movies
        3. Check if already in database / if exist, pass.
        3.  loop through each movie to query their data 
        4. Import new movies 
        """

        page_st = 1
        page_end = 1
        
        try:
            while page_st <= page_end:
                self.stdout.write(f"request importing bulk new movies\n") # debug print
                popular_movies = fetch_popular_movies(page_st)

                if not popular_movies:
                    # print(f" The query could not fetch a list of popular movies, check the url.")  # debug print
                    self.stdout.write(self.style.ERROR(f" The query could not fetch a list of popular movies, check the url.\nstatus=404"))  # debug print
                    # return JsonResponse({'message': 'Bulk import failed, check Url'}, status=404)

                self.stdout.write("\n Looping through the list of popular movies and pass the Ids to get the datas.\n")
                for tmdb_movie in popular_movies['results']:
                    tmdb_id = tmdb_movie['id']
                    self.stdout.write(f" passing tmdb_id: {tmdb_id}") # debug print

                    # Check if movie exists
                    if not Movie.objects.filter(tmdb_id=tmdb_id).exists():
                        try:
                            add_movies_from_tmdb(tmdb_id)
                            self.stdout.write(self.style.SUCCESS(f"Imported movie: {tmdb_movie['title']}"))  # not sure it is imported if already exist
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f"Error importing {tmdb_movie['title']}: {e}"))
                    else:
                        self.stdout.write(self.style.WARNING(f"{tmdb_movie['title']} already exists in DB."))


                page_st += 1
                time.sleep(2) # give some time between fetching a new page list of movies.
            self.stdout.write(self.style.SUCCESS(f"Imported list of popular movies successfully"))

        except Exception as e:
            # messages.error(request, "the page seem to experience some issue, please try again later")
            self.stdout.write(self.style.WARNING(f" error :{e}"))



    def import_series(self):
        """
        Bulk import strategy:
        1. Fetch popular list of series
        3. Check if already in database / if so, pass.
        3.  loop through each serie to query their data 
        4. Import new series 
        """

        page_st = 1
        page_end = 1
        
        try:
            while page_st <= page_end:
                self.stdout.write(f"request importing popular Series\n") # debug print
                popular_series = fetch_popular_series(page_st)

                if not popular_series:
                    self.stdout.write(self.style.ERROR(f" The query could not fetch a list of popular series, check the url.\nstatus=404"))  # debug print

                self.stdout.write("\n Looping through the list of popular series and pass the Ids to get the datas.\n")
                for tmdb_serie in popular_series['results']:
                    tmdb_id = tmdb_serie['id']
                    self.stdout.write(f" passing tmdb_id: {tmdb_id}") # debug print

                    # Check if serie exists
                    if not Serie.objects.filter(tmdb_id=tmdb_id).exists():
                        try:
                            add_series_from_tmdb(tmdb_id)
                            self.stdout.write(self.style.SUCCESS(f"Imported serie: {tmdb_serie['name']}\n"))  # not sure it is imported if already exist
                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f"Error importing {tmdb_serie['name']}: {e}"))
                    else:
                        self.stdout.write(self.style.WARNING(f"{tmdb_serie['name']} already exists in DB."))


                page_st += 1
                time.sleep(2) # give some time between fetching a new page list of series.
            self.stdout.write(self.style.SUCCESS(f"Imported list popular series done! success"))

        except Exception as e:
            self.stdout.write(self.style.WARNING(f" error :{e}"))



# ------ To import a single movie ---- Might not use in the end.
# def import_movie(request, tmdb_id):
#     '''Import a movie in making a request to TMDB api and store it in the database'''
#     print(f"request importing a new movie")
#     try:
#         if request.method == 'GET' and request.user.is_superuser:

#             try:
#                 # check if the movie is already in our database
#                 exisiting_movie = Movie.objects.get(tmdb_id=tmdb_id)
#                 print(f"Movie already exists: movie {exisiting_movie.id}: {exisiting_movie.title}")
#                 return JsonResponse({
#                     'status': 'already exists in DB', 
#                     'tmdb_id': exisiting_movie.tmdb_id, 
#                     'movie_id': exisiting_movie.id,
#                     'title': exisiting_movie.title
#                 }, status=200)
            
#             # if the movie is not then we try to fetch it.
#             except Movie.DoesNotExist:
#                 result = add_movies_from_tmdb(tmdb_id)

#                 # Determine appropriate HTTP status code
#                 status_code = {
#                     'added': 201,
#                     'exists': 200,
#                     'error': 404
#                 }.get(result['status'], 400)

#                 return JsonResponse(result, status=status_code)

#         else:
#             print(f"Unauthorized access to 'import_movie' page.")
#             messages.error(request, "You are not authorized to import movies")
#             return redirect('main:home')
        
#     except Exception as e:
#         messages.error(request, "the page seem to experience some issue, please try again later")
#         print(f" error :{e}")
#         # return JsonResponse()
#         return JsonResponse({
#             'status': 'error',
#             'message': 'An unexpected error occurred'
#         }, status=500)



# ------ To import a single serie ---- Might not use in the end.
# def import_serie(request, tmdb_id):
#     '''Import a movie in making a request to TMDB api and store it in the database'''
#     print(f"request importing a new serie")
#     try:
#         if request.method == 'GET' and request.user.is_superuser:

#             try:
#                 # check if the movie is already in our database
#                 exisiting_serie = Serie.objects.get(tmdb_id=tmdb_id)
#                 print(f"Serie already exists: serie {exisiting_serie.id}: {exisiting_serie.title}")
#                 return JsonResponse({
#                     'status': 'already exists in DB', 
#                     'tmdb_id': exisiting_serie.tmdb_id, 
#                     'serie_id': exisiting_serie.id,
#                     'title': exisiting_serie.title
#                 }, status=200)
            
#             # if the movie is not then we try to fetch it.
#             except Serie.DoesNotExist:

#                 result = add_series_from_tmdb(tmdb_id)

#                 # Determine appropriate HTTP status code
#                 status_code = {
#                     'added': 201,
#                     'exists': 200,
#                     'error': 404
#                 }.get(result['status'], 400)

#                 return JsonResponse(result, status=status_code)
#         else:
#             print(f"Unauthorized access to 'import_serie' page.")
#             messages.error(request, "You are not authorized to import series")
#             return redirect('main:home')

#     except Exception as e:
#         messages.error(request, "the page seem to experience some issue, please try again later")
#         print(f" error :{e}")
#         return JsonResponse({
#             'status': 'error',
#             'message': 'An unexpected error occurred'
#         }, status=500)
    

