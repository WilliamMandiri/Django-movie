from django.db import models

# Create your models here.
class MovieModel(models.Model):
    movie_title = models.CharField(max_length=200)
    release_date = models.DateField()
    rating = models.IntegerField(default=5)
    poster_url = models.URLField()
    synopsis = models.TextField()
    cast = models.TextField()

    def __str__(self):
        return self.movie_title

