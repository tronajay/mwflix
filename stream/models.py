from django.db import models

# Create your models here.
class Stream(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    thumbnail = models.ImageField(upload_to='stream/',default="stream/stream.png")
    description = models.TextField()

    def __str__(self):
        return self.title
    