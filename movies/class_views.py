from django.views import View
from django.shortcuts import render
from movies.models import Actor, Oscar, Movie, Country


class ActorView(View):
    def get(self, request):
        return render(
            request,
            template_name='actors.html',
            context={"actors": Actor.objects.all()}
        )


class OscarView(View):
    def get(self, request):
        return render(
            request,
            template_name="oscars.html",
            context={"oscars": Oscar.objects.all()}
        )


class MovieView(View):
    def get(self, request):
        return render(
            request,
            template_name="movies.html",
            context={"movies": Movie.objects.all()}
        )


class CountryView(View):
    def get(self, request):
        return render(
            request,
            template_name="countries.html",
            context={"countries": Country.objects.all()}
        )