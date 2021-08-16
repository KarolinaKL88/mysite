from django.urls import path
from movies import generic_views

urlpatterns = [
    path("actor-template-view/", generic_views.ActorTemplateView.as_view(), name="actor-template-view"),
    path("oscar-template-view/", generic_views.OscarTemplateView.as_view(), name="oscar-template-view"),
    path("movie-template-view/", generic_views.MovieTemplateView.as_view(), name="movie-template-view"),
    path("country-template-view/", generic_views.CountryTemplateView.as_view(), name="country-template-view"),
    path("actor-list-view/", generic_views.ActorListView.as_view(), name="actor-list-view"),
    path("oscar-list-view/", generic_views.OscarListView.as_view(), name="oscar-list-view"),
    path("movie-list-view/", generic_views.MovieListView.as_view(), name="movie-list-view"),
    path("country-list-view/", generic_views.CountryListView.as_view(), name="country-list-view"),
    path("actor-form-view/", generic_views.ActorFormView.as_view(), name='actor-form-view'),
    path("movie-form-view/", generic_views.MovieFormView.as_view(), name='movie-form-view'),
    path("oscar-form-view/", generic_views.OscarFormView.as_view(), name='oscar-form-view'),
    path("country-form-view/", generic_views.CountryFormView.as_view(), name='country-form-view'),
    path("actor-create-view/", generic_views.ActorCreateView.as_view(), name='actor-create-view'),
    path("movie-create-view/", generic_views.MovieCreateView.as_view(), name='movie-create-view'),
    path("oscar-create-view/", generic_views.OscarCreateView.as_view(), name='oscar-create-view'),
    path("country-create-view/", generic_views.CountryCreateView.as_view(), name='country-create-view'),
    path("actor-detail-view/<pk>/", generic_views.ActorDetailView.as_view(), name='actor-detail-view'),
    path("actor-update-view/<pk>/", generic_views.ActorUpdateView.as_view(), name='actor-update-view'),
    path("actor-delete-view/<pk>", generic_views.ActorDeleteView.as_view(), name='actor-delete-view'),
    path("movie-detail-view/<pk>/", generic_views.MovieDetailView.as_view(), name='movie-detail-view'),
    path("movie-update-view/<pk>/", generic_views.MovieUpdateView.as_view(), name='movie-update-view'),
    path("movie-delete-view/<pk>/", generic_views.MovieDeleteView.as_view(), name='movie-delete-view'),
    path("oscar-detail-view/<pk>/", generic_views.OscarDetailView.as_view(), name='oscar-detail-view'),
    path("oscar-update-view/<pk>/", generic_views.OscarUpdateView.as_view(), name='oscar-update-view'),
    path("oscar-delete-view/<pk>/", generic_views.OscarDeleteView.as_view(), name='oscar-delete-view'),
    path("country-detail-view/<pk>/", generic_views.CountryDetailView.as_view(), name='country-detail-view'),
    path("country-update-view/<pk>/", generic_views.CountryUpdateView.as_view(), name='country-update-view'),
    path("country-delete-view/<pk>/", generic_views.CountryDeleteView.as_view(), name='country-delete-view')
]
