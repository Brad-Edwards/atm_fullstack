from django.db import models


class Movie(models.Model):
    """Represents a movie that can be searched and displayed.

    Attributes
    ----------
    description : str
        Promotional description of movie.
    duration : int
        Length of movie in minutes.
    last_admin_update : datetime.date
        Date the movie data was last updated by a site admin.
    last_data_store_update : datetime.date
        Date the movie data was last updated from a data store.
    release_year : datetime.date
        The year the movie was released.
    title : str
        The movie's title.
    """

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField()
    duration = models.IntegerField(blank=True, null=True)
    poster_uri = models.CharField(max_length=255, blank=True, null=True)
    last_admin_update = models.DateField(blank=True, null=True)
    last_data_store_update = models.DateField(blank=True, null=True)

    def __str__(self):
        """Returns a human readable display name for the model."""
        return f"{self.title} {self.release_year.strftime('%Y')}"


class Review(models.Model):
    """Represents a review left by a user.

    Attributes
    ----------
    date: datetime.date
        Date the review was created.
    movie: Movie
        Movie associated to the review.
    rating: bool
        Like/dislike (true/false) rating of the movie.

    """

    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    rating = models.BooleanField()
    date = models.DateField()

    def __str__(self):
        """Returns a human readable display name for the model.

        Returns
        -------
        str
            admin name as ``[movie title] [review date]``.
        """
        return f"{self.movie.title} {self.date.strftime('%Y-%m-%d')}"
