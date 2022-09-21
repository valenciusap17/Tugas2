from django.db import models

# Create your models here.
class ListOfFilm(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.TextField()