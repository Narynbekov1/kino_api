from django.db import models
from datetime import date


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField('text')
    slug = models.SlugField(max_length=180, primary_key=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Actor(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=150)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField('text')
    image = models.ImageField(upload_to='actors/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Actor and Director'
        verbose_name_plural = 'Actors and Directors'


class ActorImage(models.Model):
    image = models.ImageField(upload_to='actors', blank=True, null=True)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name='images')


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField('text')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'


class Movie(models.Model):
    title = models.CharField(max_length=150)
    tagline = models.CharField(max_length=100, default='')
    description = models.TextField('text')
    poster = models.ImageField(upload_to='movies/')
    year = models.PositiveSmallIntegerField(default='2022')
    country = models.CharField(max_length=40)
    directors = models.ManyToManyField(Actor, verbose_name='Director', related_name='film_director')
    actors = models.ManyToManyField(Actor, verbose_name='Actor', related_name='film_actor')
    genres = models.ManyToManyField(Genre, verbose_name='Genre')
    world_premiere = models.DateField(default=date.today)
    budget = models.PositiveIntegerField('Budget', default=0, help_text='enter the dollar amount')
    fess_in_world = models.PositiveIntegerField(default=0, help_text='enter the dollar amount')
    fess_in_usa = models.PositiveIntegerField(default=0, help_text='enter the dollar amount')
    category = models.ForeignKey(
        Category, verbose_name='Category', on_delete=models.SET_NULL, null=True
    )
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


# class MovieShots(models.Model):
#     title = models.CharField(max_length=150)
#     description = models.TextField('text')
#     image = models.ImageField(upload_to='movie_shots/')
#     movie = models.ForeignKey(Movie, verbose_name='Movie', on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'film frame'
#         verbose_name_plural = 'film stills'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    # parent = models.ForeignKey(
    #     'self', verbose_name='Genus', on_delete=models.SET_NULL, blank=True, null=True
    # )
    movie = models.ForeignKey(Movie, verbose_name='Movie', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'





