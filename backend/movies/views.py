from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from movies.models import Movie, Review
from movies.serializers import MovieSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class MovieListView(APIView):
    def get(self, request, format=None):
        movies = Movie.objects.all()                                  
        movie_serializer = MovieSerializer(movies, many=True)
        return JsonResponse(movie_serializer.data, safe=False)

    def post(self, request, format=None):
        movie_data = JSONParser().parse(request)
        movie_serializer = MovieSerializer(data=movie_data)

        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(movie_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(APIView):
    def get(self, request, pk, format=None):
        try: 
            movie = Movie.objects.get(pk=pk) 
        except Movie.DoesNotExist: 
            return JsonResponse({'message': 'The Movie does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
        movie_serializer = MovieSerializer(movie)
        return JsonResponse(movie_serializer.data)

    def put(self, request, pk, format=None):
        try: 
            movie = Movie.objects.get(pk=pk) 
        except Movie.DoesNotExist: 
            return JsonResponse({'message': 'The Movie does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        movie_data = JSONParser().parse(request)
        movie_serializer = MovieSerializer(movie, data=movie_data)

        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(movie_serializer.data)
        return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try: 
            movie = Movie.objects.get(pk=pk) 
        except Movie.DoesNotExist: 
            return JsonResponse({'message': 'The Movie does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        movie.delete()
        return JsonResponse({'message': 'Movie was deleted successfully.'})


class ReviewListView(APIView):
    def get(self, request, format=None):
        reviews = Review.objects.all()                                  
        review_serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(review_serializer.data, safe=False)

    def post(self, request, format=None):
        review_data = JSONParser().parse(request)
        review_serializer = ReviewSerializer(data=review_data)

        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse(review_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailView(APIView):
    def get(self, request, pk, format=None):
        try: 
            review = Review.objects.get(pk=pk) 
        except Review.DoesNotExist: 
            return JsonResponse({'message': 'The Review does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
        review_serializer = ReviewSerializer(review)
        return JsonResponse(review_serializer.data)

    def put(self, request, pk, format=None):
        try: 
            review = Review.objects.get(pk=pk) 
        except Review.DoesNotExist: 
            return JsonResponse({'message': 'The Review does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        review_data = JSONParser().parse(request)
        review_serializer = ReviewSerializer(review, data=review_data)

        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse(review_serializer.data)
        return JsonResponse(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try: 
            review = Review.objects.get(pk=pk) 
        except Review.DoesNotExist: 
            return JsonResponse({'message': 'The Review does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        review.delete()
        return JsonResponse({'message': 'Review was deleted successfully.'})