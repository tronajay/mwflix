from django.db import models

MOVIE_CAT = (
    ("Movie", "Movie"),
    ("TV Show", "TV Show"),
    ("Short Film", "Short Film"),
)


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
    thumbnail = models.ImageField(upload_to='movies/',blank=True)
    description = models.TextField()
    rating = models.FloatField(default=0)
    released = models.DateField(auto_now=False)

    def __str__(self):
        return self.title
    