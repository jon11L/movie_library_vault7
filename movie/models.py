from django.db import models

class Movie(models.Model):

    # External unique identifier / sources for api references
    tmdb_id = models.IntegerField(unique=True, null=True, blank=True)  # allow to find the content id in TMDB
    imdb_id = models.CharField(max_length=20, blank=True, null=True) # same as above

    # Core Movie Details
    original_title = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    release_date = models.DateField(blank=True, null=True)
    origin_country = models.JSONField(blank=True, null=True)
    original_language = models.CharField(max_length=50, blank=True, null=True)  # Movie's original language
    production = models.JSONField(blank=True, null=True)
    director = models.JSONField(blank=True, null=True)
    writer = models.JSONField(blank=True, null=True)
    casting = models.JSONField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True) # will display the Movie time in minutes
    description = models.TextField(max_length=1000, blank=True, null=True)
    genre = models.JSONField(blank=True, null=True)  # This field an array of strings, i want 
    budget = models.IntegerField(blank=True, null=True)
    revenue = models.BigIntegerField(blank=True, null=True)  # Movie's box office revenue
    released = models.BooleanField(blank=True, null=True)
    tagline = models.TextField(blank=True, null=True)  # Movie's tagline/slogan
    # spoken_language = models.CharField(blank=True, null=True) # take from the list of dict: ['spokent_languages'] "english_name"

    # Metrics
    vote_average = models.FloatField(blank=True, null=True)  # for TMDB rating
    vote_count = models.IntegerField(blank=True, null=True)  
    imdb_rating = models.FloatField(blank=True, null=True)  # to fetch externally their rating
    popularity = models.FloatField(blank=True, null=True)  
    # images
    image_poster = models.URLField(blank=True, null=True) # vertical poster ( made for list,dvd format..)
    banner_poster = models.URLField(blank=True, null=True) # banner image ( wide format)
    # trailers
    trailer_youtube_id = models.CharField(max_length=11, blank=True, null=True)  # YouTube id of the movie's trailer // append this later for the links: https://www.youtube.com/watch?v=

    # would serve to implement a check if a movie has a follow up, or part of a trilogy?
    # has_siblings = models.BooleanField(default=False)

    # Time stamp
    added_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        db_table = 'movie'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'

    
    def __str__(self):
        return self.title
    

    # The below functions are to format the fields for a better human readable display.

    def render_genre(self):
        '''return the Movie.genre attribute in without quotes and [],
        only comma-separated string.
        '''
        if self.genre:
            genre = ', '.join(self.genre)
            return genre
        else:
            return 'N/a'
    
    
    def render_casting(self):
        '''return the Movie.casting attribute in without quotes and [],
        only comma-separated string.
        '''
        if self.casting:
            casting = ', '.join([f"{cast['name']} as {cast['role']}" for cast in self.casting])
            return casting
        return 'N/a'


    def render_writer(self):
        '''return the Movie.writer attribute in without quotes and [],
        only comma-separated string.
        '''
        if self.writer:
            writer = ', '.join(self.writer)
            return writer
        return 'N/a'
    
    def render_production(self):
        '''return the Movie.production attribute in without quotes and [],
        only comma-separated string.
        '''
        if self.production:
            production = ', '.join(self.production)
            return production 
        return 'N/a'   

    def render_director(self):
        '''return the Movie.director attribute in without quotes and [],
        only comma-separated string.
        '''
        if self.director:
            director = ', '.join(self.director)
            return director
        return 'N/a'


    def render_vote_average(self):
        '''return the Movie.vote_average with a rounded number'''
        if self.vote_average:
            return round(self.vote_average, 1)
        else:
            return 0
        

    def render_origin_country(self):
        '''return the Movie.origin_country with a comma-separated string'''
        if self.origin_country:
            origin_country = ', '.join(self.origin_country)
            return origin_country  
        return 'N/a' 
    
    def render_length(self):
        '''return the Movie.length with a formatted string
        (e.g., 1h 30m)
        '''
        if self.length:
            minutes = self.length % 60
            hours = self.length // 60
            if hours == 0:
                return f'{minutes}min'
            
            elif hours > 0 and minutes <= 9:
                return f'{hours}h0{minutes}'
            else:
                return f'{hours}h{minutes}'
        return 'N/a'
    

    def render_link_youtube(self):
        ''' concatenates the field "trailer_youtube_id" 
        to the base url
        '''
        if self.trailer_youtube_id:
            trailer_link = f'https://www.youtube.com/watch?v={self.trailer_youtube_id}'
            return trailer_link
        return 'Trailer Not found'