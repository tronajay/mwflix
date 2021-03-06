from django.shortcuts import redirect, render
from .models import Genre, Movie, Production
from django.core.paginator import Paginator

def genres(request):
    return {'genre': Genre.objects.all()}

def home(request):
    movie = Paginator(Movie.objects.all().order_by('released')[::-1],18)
    page = request.GET.get('page')
    movies = movie.get_page(page)
    params = {'movies':movies}
    return render(request,'movies/movies-list.html',params)

def moviepage(request,slug):
    movie = Movie.objects.get(slug=slug)
    params = {'movie':movie}
    return render(request,'movies/movie-page.html',params)

def moviegenre(request,slug):
    genre = Genre.objects.get(slug=slug)
    movie = Paginator(Movie.objects.filter(genre__id=genre.id).order_by('released')[::-1],18)
    page = request.GET.get('page')
    movies = movie.get_page(page)
    params = {'movies':movies}
    return render(request,'movies/movies-list.html',params)

def movies(request):
    movie = Paginator(Movie.objects.filter(category="Movie").order_by('released')[::-1],18)
    page = request.GET.get('page')
    movies = movie.get_page(page)
    params = {'movies':movies}
    return render(request,'movies/movies-list.html',params)

def tvshows(request):
    movie = Paginator(Movie.objects.filter(category="TV Show").order_by('released')[::-1],18)
    page = request.GET.get('page')
    movies = movie.get_page(page)
    params = {'movies':movies}
    return render(request,'movies/movies-list.html',params)

def shortfilm(request):
    movie = Paginator(Movie.objects.filter(category="Short Film").order_by('released')[::-1],18)
    page = request.GET.get('page')
    movies = movie.get_page(page)
    params = {'movies':movies}
    return render(request,'movies/movies-list.html',params)

def search(request):
    if request.method=="GET":
        query = request.GET['q']
        movie = Paginator(Movie.objects.filter(title__icontains=query),18)
        page = request.GET.get('page')
        movies = movie.get_page(page)
        params = {'movies':movies}
        return render(request,'movies/movies-list.html',params)
    else:
        return redirect("/")
    
def production(request,slug):
    movie = Paginator(Movie.objects.filter(production__slug=slug).order_by('released')[::-1],18)
    page = request.GET.get('page')
    movies = movie.get_page(page)
    stream = Production.objects.get(slug=slug)
    params = {'movies':movies,'stream':stream}
    return render(request,'movies/movies-list.html',params)