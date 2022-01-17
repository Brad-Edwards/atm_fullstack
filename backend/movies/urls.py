from django.urls import path
from movies import views 

# /api/movies GET, POST, DELETE
# /api/movies GET, PUT, DELETE
# /api/reviews GET, POST, DELETE

urlpatterns = [
    path("movies", views.movie_list),
    path("movies/?P<pk>[0-9]+)", views.movie_detail),
    path("reviews", views.review_list)
]
