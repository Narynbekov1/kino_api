from django.urls import path
from film import views

urlpatterns = [
    path('categories/', views.categories, name='categories-list'),
    path('actors/', views.ActorView.as_view(), name='actors-list'),
    path('actors/<int:pk>/', views.ActorDetailView.as_view(), name='actor-detail'),
    path('actors-update/<int:pk>/', views.ActorUpdateView.as_view()),
    path('actors-delete/<int:pk>/', views.ActorDeleteView.as_view()),
    path('genres/', views.GenreListView.as_view(), name='genre-list'),
    path('movie/', views.MovieListView.as_view(), name='movie-list'),
    path('reviews/', views.ReviewsListView.as_view(), name='reviews-list'),
    path('ratingStar/', views.RatingStarListView.as_view(), name='ratingStar-list'),
]