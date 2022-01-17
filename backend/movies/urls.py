from django.urls import path, include
from movies import views 

# /api/movies GET, POST, DELETE
# /api/movies GET, PUT, DELETE
# /api/reviews GET, POST, DELETE

urlpatterns = [
    path("movies", views.MovieListView.as_view()),
    path("movies/<int:pk>", views.MovieDetailView.as_view()),    
    path("reviews", views.ReviewListView.as_view()),
    path("reviews/<int:pk>", views.ReviewDetailView.as_view())
]
