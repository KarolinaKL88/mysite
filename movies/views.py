from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from movies.models import Actor, Movie, Country, Oscar
from movies.forms import ActorForm, CountryForm, MovieForm, OscarForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test

# Create your views here.

@login_required(login_url="accounts/login/")
def actors(request):
    return render(
        request,
        template_name='actors.html',
        context={"actors": Actor.objects.all()}
    )


def movies(request):
    return render(
        request,
        template_name='movies.html',
        context={"movies": Movie.objects.all()}
    )


def countries(request):
    return render(
        request,
        template_name='countries.html',
        context={"countries": Country.objects.all()}
    )


def oscars(request):
    return render(
        request,
        template_name='oscars.html',
        context={"oscars": Oscar.objects.all()}
    )


def index2(request):
    return render(
        request,
        template_name='index2.html'
    )


def actor_form(request):
    form = ActorForm(request.POST or None)
    if form.is_valid():
        my_name = form.cleaned_data["name"]
        my_last_name = form.cleaned_data["last_name"]
        my_age = form.cleaned_data["age"]
        my_gender = form.cleaned_data["gender"]
        Actor.objects.create(name=my_name, last_name=my_last_name, age=my_age, gender=my_gender)
        return HttpResponseRedirect(reverse('actors'))
    return render(
        request,
        template_name="form.html",
        context={"form": form}
    )


def movie_form(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        my_title = form.cleaned_data["title"]
        my_genre = form.cleaned_data["genre"]
        my_year = form.cleaned_data["year"]
        my_actor = form.cleaned_data["actor"]
        my_country = form.cleaned_data["country"]
        Movie.objects.create(title=my_title, genre=my_genre, year=my_year, actor=my_actor, country=my_country)
        return HttpResponseRedirect(reverse('movies'))
    return render(
        request,
        template_name='form.html',
        context={'form': form}
    )


def oscar_form(request):
    form = OscarForm(request.POST or None)
    if form.is_valid():
        my_category = form.cleaned_data["category"]
        my_year = form.cleaned_data["year"]
        my_movie = form.cleaned_data["movie"]
        my_actor = form.cleaned_data["actor"]
        my_oscar = Oscar.objects.filter(category=my_category, year=my_year, movie=my_movie, actor=my_actor)
        if my_oscar:
            return HttpResponseRedirect(reverse('oscars'))
        Oscar.objects.create(category=my_category, year=my_year, movie=my_movie, actor=my_actor)
        return HttpResponseRedirect(reverse('oscars'))
    return render(
        request,
        template_name='form.html',
        context={'form': form}
    )


def country_form(request):
    form = CountryForm(request.POST or None)
    if form.is_valid():
        my_name = form.cleaned_data["name"]
        my_iso_code = form.cleaned_data["iso_code"]
        Country.objects.create(name=my_name, iso_code=my_iso_code)
        return HttpResponseRedirect(reverse('countries'))
    return render(
        request,
        template_name='form.html',
        context={'form': form}
    )
