from django.db import models
from stream.models import Stream

MOVIE_CAT = (
    ("Movie", "Movie"),
    ("TV Show", "TV Show"),
    ("Short Film", "Short Film"),
)
MOVIE_STATUS = (
    ("Upcoming", "Upcoming"),
    ("Released", "Released"),
    ("Digital", "Digital"),
)

class Production(models.Model):
    title =  models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    thumbnail = models.ImageField(upload_to='production/',default="production/default.png")
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Genre(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    category = models.CharField(choices=MOVIE_CAT,max_length=200,default="Movie")
    genre = models.ManyToManyField(Genre)
    production = models.ManyToManyField(Production,default=1)
    status = models.CharField(choices=MOVIE_STATUS,max_length=50,default="Released")
    platform = models.ManyToManyField(Stream,blank=True)
    thumbnail = models.ImageField(upload_to='movies/',blank=True)
    description = models.TextField()
    rating = models.CharField(max_length=10,default="0")
    released = models.DateField(auto_now=False)

    def __str__(self):
        return self.title
    