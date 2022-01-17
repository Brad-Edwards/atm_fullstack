from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from movies.models import Movie, Review
from movies.serializers import MovieSerializer
from rest_framework.decorators import api_view

@api_view(['GET', 'POST', 'DELETE'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movies.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            movies = movies.filter(title__icontains=title)

    elif request.method == 'POST':
        movie_data = JSONParser().parse(request)
        movie_serializer = MovieSerializer(data=movie_data)

        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(movie_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, pk):
    try: 
        tutorial = Tutorial.objects.get(pk=pk) 
    except Tutorial.DoesNotExist: 
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        movie_serializer = MovieSerializer(movie)
        return JsonResponse(movie_serializer.data)

    elif request.method == 'PUT':
        movie_data = JSONParser().parse(request)
        movie_serializer = MovieSerializer(movie, data=movie_data)

        if movie_serializer.is_valid():
            movie_serializer.save()
            return JsonResponse(movie_serializer.data)
        return JsonResponse(movie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        movie.delete()
        return JsonResponse({'message': 'Movie was deleted successfully.'})

@api_view(['GET', 'POST'])
def review_list(request):
    if request.method == 'GET':
        reviews = Review.objects.all()

        movie_id = request.GET.get('movie', None)
        if movie_id is not None:
            reviews = reviews.filter(movie=int(movie_id))    
   
    elif request.method == 'POST':
        review_data = JSONParser().parse(request)
        review_serializer = MovieSerializer(data=review_data)

        if review_serializer.is_valid():
            review_serializer.save()
            return JsonResponse(review_serializer.data, status=status.HTTP_201_CREATED)            
        return JsonResponse(review_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
