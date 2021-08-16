from  django import forms

from movies.models import Actor, Oscar, Movie, Country

class ActorForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    last_name = forms.CharField(max_length=128)
    age = forms.IntegerField()
    gender = forms.CharField(max_length=1)

    class Meta:
        model = Actor
        fields = "__all__"


class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=128)
    genre = forms.CharField(max_length=128)
    year = forms.IntegerField()
    actor = forms.ModelChoiceField(queryset=Actor.objects.all())
    country = forms.ModelChoiceField(queryset=Country.objects.all())

    class Meta:
        model = Movie
        fields = "__all__"

class OscarForm(forms.ModelForm):
    category = forms.CharField(max_length=128)
    year = forms.IntegerField()
    movie = forms.ModelChoiceField(queryset=Movie.objects.all())
    actor = forms.ModelChoiceField(queryset=Actor.objects.all())

    class Meta:
        model = Oscar
        fields = "__all__"


class CountryForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    iso_code = forms.CharField(max_length=3)

    class Meta:
        model = Country
        fields = "__all__"
