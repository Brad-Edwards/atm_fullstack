from django.urls import path, include
from movies import views 

# /api/movies GET, POST, DELETE
# /api/movies GET, PUT, DELETE
# /api/reviews GET, POST, DELETE

urlpatterns = [
    path("movies", views.MovieListView.as_view()),  # GET, POST
    path("movies/<int:pk>", views.MovieDetailView.as_view()),  # GET, PUT, DELETE  
    path("reviews", views.ReviewListView.as_view()),  # GET, POST
    path("reviews/<int:pk>", views.ReviewDetailView.as_view())  # GET, PUT, DELETE
]
