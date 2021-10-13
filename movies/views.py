from django.db import models
from django.shortcuts import render
from .models import Genre, Movie

def home(request):
    movies = Movie.objects.all()
    params = {'movies':movies}
    return render(request,'movies/movies-list.html',params)

def moviepage(request,slug):
    movie = Movie.objects.get(slug=slug)
    params = {'movie':movie}
    return render(request,'movies/movie-page.html',params)

def moviegenre(request,slug):
    genre = Genre.objects.get(slug=slug)
    movies = Movie.objects.filter(genre__id=genre.id)
    params = {'movies':movies}
    return render(request,'movies/movies-list.html',params)

def movies(request):
    movies = Movie.objects.filter(category="Movie")
    params = {'movies':movies}
    return render(request,'movies/movies-list.html',params)

def tvshows(request):
    movies = Movie.objects.filter(category="TV Shows")
    params = {'movies':movies}
    return render(request,'movies/movies-list.html',params)

def shortfilm(request):
    movies = Movie.objects.filter(category="Short Film")
    params = {'movies':movies}
    return render(request,'movies/movies-list.html',params)