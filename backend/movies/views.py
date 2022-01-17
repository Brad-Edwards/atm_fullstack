from django.shortcuts import render
import datetime
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from movies.models import Movie, Review
from movies.serializers import MovieSerializer, ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# TODO: view tests
class MovieListView(APIView):
    """A list of movies, optionally filtered by partial title"""
    def get(self, request, format=None):
        """Handles GET requests for all movies and filters on partial 
        title if one is given.
        
        Paramaters
        ----------
        request : Request
            The HTTP request received from the client.
            """
        movies = Movie.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            movies = movies.filter(title__icontains=title)

        movie_serializer = MovieSerializer(movies, many=True)
        return JsonResponse(movie_serializer.data, safe=False)

    def post(self, request, format=None):
        """Handles movie POST request to add a new movie to database.
        
        Attributes
        ----------
        request : Request
            The HTTP request received from the client.

        Errors
        ------
        HTTP_400_BAD_REQUEST
            Thrown if movie JSON data cannot be parsed.
        """
        movie_data = JSONParser().parse(request)
        release_year = request.POST.get('release_year', None)
        movie_serializer = MovieSerializer(data=movie_data)

        if release_year < 1900 or release_year > int(datetime.today().strftime("%Y")) + 10:
            return JsonResponse(movie_serializer.errors, status.HTTP_400_BAD_REQUEST)
        

        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(movie_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieDetailView(APIView):
    """The information about a single movie."""
    def get(self, request, pk, format=None):
        """Handles GET requests for a single movie instance.
        
        Parameters
        ----------
        request : Request
            The HTTP request received from the client.
        pk : int
            The primary key of the target movie.
            
        Errors:
            HTTP_404_NOT_FOUND
                Thrown if there is no movie with the given primary key.
        """
        try: 
            movie = Movie.objects.get(pk=pk) 
        except Movie.DoesNotExist: 
            return JsonResponse({'message': 'The Movie does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
        movie_serializer = MovieSerializer(movie)
        return JsonResponse(movie_serializer.data)

    def put(self, request, pk, format=None):
        """Handles PUT requests to update a single movie.
    
        Parameters
        ----------
        request : Request
            The HTTP request received from the client.
        pk : int
            The primary key of the target movie.
            
        Errors:
            HTTP_400_BAD_REQUEST
                Thrown if the movie JSON cannot be parsed.
            HTTP_404_NOT_FOUND
                Thrown if there is no movie with the given primary key.
        """
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
        """Handles DELETE requests to remove a single movie.
        
        Attributes
        ----------
        request : Request
            The HTTP request received from the client.
        pk : int
            The primary key of the target movie.
            
        Errors
        ------
        HTTP_404_NOT_FOUND
            Thrown if there is no movie with the primary key."""
        try: 
            movie = Movie.objects.get(pk=pk) 
        except Movie.DoesNotExist: 
            return JsonResponse({'message': 'The Movie does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        movie.delete()
        return JsonResponse({'message': 'Movie was deleted successfully.'})

#TODO: filter on movie 
class ReviewListView(APIView):
    "A list of reviews"
    def get(self, request, format=None):
        """Handles GET requests for all reviews
                
        Paramaters
        ----------
        request : Request
            The HTTP request received from the client.
            """
        reviews = Review.objects.all()

        movie_id = request.GET.get('id', None)
        if movie_id is not None:
            reviews = Review.objects.filter(movie=movie_id)

        review_serializer = ReviewSerializer(reviews, many=True)
        return JsonResponse(review_serializer.data, safe=False)

    def post(self, request, format=None):
        """Handles review POST request to add a new review to database.
        
        Attributes
        ----------
        request : Request
            The HTTP request received from the client.

        Errors
        ------
        HTTP_400_BAD_REQUEST
            Thrown if review JSON data cannot be parsed.
        """
        review_data = JSONParser().parse(request)
        review_serializer = ReviewSerializer(data=review_data)

        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse(review_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailView(APIView):
    """Information about a single review."""
    def get(self, request, pk, format=None):
        """Handles GET requests for a single review instance.
        
        Parameters
        ----------
        request : Request
            The HTTP request received from the client.
        pk : int
            The primary key of the target review.
            
        Errors:
            HTTP_404_NOT_FOUND
                Thrown if there is no review with the given primary key.
        """
        try: 
            review = Review.objects.get(pk=pk) 
        except Review.DoesNotExist: 
            return JsonResponse({'message': 'The Review does not exist'}, status=status.HTTP_404_NOT_FOUND) 
    
        review_serializer = ReviewSerializer(review)
        return JsonResponse(review_serializer.data)

    def put(self, request, pk, format=None):
        """Handles review POST request to add a new review to database.
        
        Attributes
        ----------
        request : Request
            The HTTP request received from the client.

        Errors
        ------
        HTTP_400_BAD_REQUEST
            Thrown if review JSON data cannot be parsed.
        """
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
        """Handles DELETE requests to remove a single review.
        
        Attributes
        ----------
        request : Request
            The HTTP request received from the client.
        pk : int
            The primary key of the target review.
            
        Errors
        ------
        HTTP_404_NOT_FOUND
            Thrown if there is no review with the primary key."""
        try: 
            review = Review.objects.get(pk=pk) 
        except Review.DoesNotExist: 
            return JsonResponse({'message': 'The Review does not exist'}, status=status.HTTP_404_NOT_FOUND) 
        review.delete()
        return JsonResponse({'message': 'Review was deleted successfully.'})