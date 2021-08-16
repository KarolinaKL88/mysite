from django.urls import path
from movies import class_views

urlpatterns = [
    path("actor-class-view/", class_views.ActorView.as_view(), name="actor-class-view"),
    path("movie-class-view/", class_views.MovieView.as_view(), name="movie-class-view"),
    path("oscar-class-view/", class_views.OscarView.as_view(), name="oscar-class-view"),
    path("country-class-view/", class_views.CountryView.as_view(), name="country-class-view"),
]