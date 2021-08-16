from django.db import models


# Create your models here.
class Actor(models.Model):
    gender_choices = [('M', 'Male'),
                      ('F', 'Female')]
    name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=gender_choices)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class Country(models.Model):
    name = models.CharField(max_length=128)
    iso_code = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.name}"


class Movie(models.Model):
    title = models.CharField(max_length=128)
    genre = models.CharField(max_length=128)
    year = models.IntegerField()
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, null=True, blank=True, related_name="movies")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True, related_name="movies")

    def __str__(self):
        return f"{self.title}, {self.year}"


class Oscar(models.Model):
    category = models.CharField(max_length=128)
    year = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, blank=True, related_name="oscars")
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, null=True, blank=True, related_name="oscars")

    def __str__(self):
        return f"{self.category}, {self.year}, {self.movie}, {self.actor}"
