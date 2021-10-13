
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('movie/<str:slug>',views.moviepage,name="moviepage"),
    path('genre/<str:slug>',views.moviegenre,name="moviegenre"),
    path('movies',views.movies,name="movies"),
    path('tv-shows',views.tvshows,name="tvshows"),
    path('short-films',views.shortfilm,name="shortfilm"),
]
