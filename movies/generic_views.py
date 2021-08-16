from django.views.generic import DetailView, FormView, ListView, UpdateView, DeleteView, TemplateView, CreateView
from movies.models import Actor, Oscar, Movie, Country
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from movies.forms import ActorForm, MovieForm, OscarForm, CountryForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

class ActorTemplateView(TemplateView):
    login_url = reverse_lazy('homepage')
    template_name = "actors.html"
    extra_context = {"actors": Actor.objects.all()}


class MovieTemplateView(TemplateView):
    login_url = reverse_lazy('homepage')
    template_name = "movies.html"
    extra_context = {"movies": Movie.objects.all()}


class OscarTemplateView(TemplateView):
    login_url = reverse_lazy('homepage')
    template_name = "oscars.html"
    extra_context = {"oscars": Oscar.objects.all()}


class CountryTemplateView(TemplateView):
    login_url = reverse_lazy('homepage')
    template_name = "countries.html"
    extra_context = {"countries": Country.objects.all()}


class ActorListView(ListView):
    login_url = reverse_lazy('homepage')
    template_name = "list2.html"
    model = Actor


class MovieListView(ListView):
    login_url = reverse_lazy('homepage')
    template_name = "list2.html"
    model = Movie


class OscarListView(ListView):
    login_url = reverse_lazy('homepage')
    template_name = "list2.html"
    model = Oscar


class CountryListView(ListView):
    login_url = reverse_lazy('homepage')
    template_name = "list2.html"
    model = Country


class ActorFormView(FormView):
    login_url = reverse_lazy('homepage')
    template_name = "form.html"
    form_class = ActorForm
    success_url = reverse_lazy("actors")

    def form_valid(self, form):
        my_name = form.cleaned_data["name"]
        my_last_name = form.cleaned_data["last_name"]
        my_age = form.cleaned_data["age"]
        my_gender = form.cleaned_data["gender"]
        Actor.objects.create(name=my_name, last_name=my_last_name, age=my_age, gender=my_gender)
        return HttpResponseRedirect(self.get_success_url())


class MovieFormView(FormView):
    login_url = reverse_lazy('homepage')
    template_name = "form.html"
    form_class = MovieForm
    success_url = reverse_lazy("movies")

    def form_valid(self, form):
        my_title = form.cleaned_data["title"]
        my_genre = form.cleaned_data["genre"]
        my_year = form.cleaned_data["year"]
        my_actor = form.cleaned_data["actor"]
        my_country = form.cleaned_data["country"]
        Movie.objects.create(title=my_title, genre=my_genre, year=my_year, actor=my_actor, country=my_country)
        return HttpResponseRedirect(self.get_success_url())


class OscarFormView(FormView):
    login_url = reverse_lazy('homepage')
    template_name = "form.html"
    form_class = OscarForm
    success_url = reverse_lazy("oscars")

    def form_valid(self, form):
        my_category = form.cleaned_data["category"]
        my_year = form.cleaned_data["year"]
        my_movie = form.cleaned_data["movie"]
        my_actor = form.cleaned_data["actor"]
        Oscar.objects.create(category=my_category, year=my_year, movie=my_movie, actor=my_actor)
        return HttpResponseRedirect(self.get_success_url())


class CountryFormView(FormView):
    login_url = reverse_lazy('homepage')
    template_name = "form.html"
    form_class = CountryForm
    success_url = reverse_lazy("countries")

    def form_valid(self, form):
        my_name = form.cleaned_data["name"]
        my_iso_code = form.cleaned_data["iso_code"]
        Country.objects.create(name=my_name, iso_code=my_iso_code)
        return HttpResponseRedirect(self.get_success_url())


# CRUD
class ActorCreateView(CreateView):
    login_url = reverse_lazy('homepage')
    model = Actor
    template_name = 'form.html'
    success_url = reverse_lazy('actors')
    form_class = ActorForm


class MovieCreateView(CreateView):
    model = Movie
    template_name = 'form.html'
    success_url = reverse_lazy('movies')
    form_class = MovieForm


class OscarCreateView(CreateView):
    model = Oscar
    template_name = 'form.html'
    success_url = reverse_lazy('oscars')
    form_class = OscarForm


class CountryCreateView(CreateView):
    model = Country
    template_name = 'form.html'
    success_url = reverse_lazy('countries')
    form_class = CountryForm


class ActorDetailView(DetailView):
    model = Actor
    template_name = "objects.html"
    extra_context = {
        "update_url": 'actor-update-view',
        "delete_url": 'actor-delete-view'
    }


class MovieDetailView(DetailView):
    model = Movie
    template_name = "objects.html"
    extra_context = {
        "update_url": "movie-update-view",
        "delete_url": "movie-delete-view"
    }


class OscarDetailView(DetailView):
    model = Oscar
    template_name = "objects.html"
    extra_context = {
        "update_url": "oscar-update-view",
        "delete_url": "oscar-delete-view"
    }


class CountryDetailView(DetailView):
    model = Country
    template_name = "objects.html"
    extra_context = {
        "update_url": "country-update-view",
        "delete_url": "country-delete-view"
    }


class ActorUpdateView(UpdateView):
    model = Actor
    fields = ("name", "last_name", "gender",)
    template_name = "form.html"
    success_url = reverse_lazy("actors")


class MovieUpdateView(UpdateView):
    model = Movie
    fields = ("title", "year")
    template_name = "form.html"
    success_url = reverse_lazy("movies")


class OscarUpdateView(UpdateView):
    model = Oscar
    fields = ("category", "year", "movie", "actor")
    template_name = "form.html"
    success_url = reverse_lazy("oscars")


class CountryUpdateView(UpdateView):
    model = Country
    fields = "__all__"
    template_name = "form.html"
    success_url = reverse_lazy("countries")


class ActorDeleteView(DeleteView):
    model = Actor
    template_name = 'delete.html'
    success_url = reverse_lazy('actors')


class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'delete.html'
    success_url = reverse_lazy('movies')


class OscarDeleteView(DeleteView):
    model = Oscar
    template_name = 'delete.html'
    success_url = reverse_lazy('oscars')


class CountryDeleteView(DeleteView):
    model = Country
    template_name = 'delete.html'
    success_url = reverse_lazy('countries')
