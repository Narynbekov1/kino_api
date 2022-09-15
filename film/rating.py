from django.db import models
from .models import Movie


class RatingStar(models.Model):
    value = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Star'
        verbose_name_plural = 'Stars'


class Rating(models.Model):
    ip = models.CharField('Ip', max_length=20)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='star')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name='film')

    def __str__(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
