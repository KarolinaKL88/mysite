from django.urls import path
from . import views

urlpatterns = [
    path('actors/', views.actors, name='actors'),
    path('movies/', views.movies, name='movies'),
    path('countries/', views.countries, name='countries'),
    path('oscars/', views.oscars, name='oscars'),
    path('index2/', views.index2, name='index2'),
    path('actor-form/', views.actor_form, name="actor-form"),
    path('movie-form/', views.movie_form, name="movie-form"),
    path('oscar-form/', views.oscar_form, name="oscar-form"),
    path('country-form/', views.country_form, name="country-form")
]