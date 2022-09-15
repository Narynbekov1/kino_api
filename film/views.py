from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Category, Actor, Genre, ActorImage, Movie, Reviews
from .rating import RatingStar
from .serializers import CategorySerializer, ActorSerializer, GenreSerializer, MovieSerializer, ReviewsSerializer, \
    RatingStarSerializer


@api_view(['GET'])
def categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


# class ActorListView(APIView):
#
#      def get(self, request):
    #     actors = Actor.objects.all()
    #     serializer = ActorSerializer(actors, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     actor = request.data
    #     serializer = ActorSerializer(data=actor)
    #     if serializer.is_valid(raise_exception=True):
    #         actor_saved = serializer.save()
    #     return Response(serializer.data)


class ActorView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetailView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorUpdateView(generics.UpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDeleteView(generics.DestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorImageView(generics.ListAPIView):
    queryset = ActorImage.objects.all()
    serializer_class = ActorSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class MovieListView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ReviewsListView(generics.ListAPIView):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer


class RatingStarListView(generics.ListAPIView):
    queryset = RatingStar.objects.all()
    serializer_class = RatingStarSerializer

# class MovieShotListView(generics.ListAPIView):
#     queryset = MovieShots.objects.all()
#     serializer_class = MovieShotsSerializer


