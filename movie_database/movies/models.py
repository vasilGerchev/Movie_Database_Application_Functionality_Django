from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    director = models.CharField(max_length=255, default='')
    release_date = models.IntegerField(default='')
    user_rating = models.FloatField(default='')
    genre = models.CharField(max_length=100, default= '')

    def __str__(self):
        return self.title
