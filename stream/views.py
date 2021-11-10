from django.shortcuts import render
from movies.models import Movie
from .models import Stream

# Create your views here.
def platforms(request):
    return render(request,'stream/platforms.html')

def stream(request,slug):
    movies = Movie.objects.filter(platform__slug=slug)
    stream = Stream.objects.get(slug=slug)
    params = {'movies':movies,'stream':stream}
    return render(request,'movies/movies-list.html',params)