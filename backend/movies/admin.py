from django.contrib import admin

from movies.models import Movie, Review


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    model = Movie


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
