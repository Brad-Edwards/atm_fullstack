import datetime

from django.test import TestCase

from movies.models import Movie, Review


class MovieTestCase(TestCase):
    """Tests cases for movies.models.Movie

    Attributes
    ----------
    ensemble_title : str
        Title for test data movie
    """
    ensemble_title = "Ensemble Force"

    def setUp(self):
        Movie.objects.create(
            description="A very excellent sci-fi movie",
            duration=150,
            poster_uri="https://movies.com",
            release_year=datetime.date(2021, 1, 1),
            title=self.ensemble_title,
        )

    def test_movies_admin_str_is_name_release_year(self):
        """Should return a str as ``[title] [release year]`` (i.e. ``The Matrix 1999``)."""
        assembly_title = "What If: We only had Assembly"
        Movie.objects.create(
            description="Not a very good movie",
            duration=400,
            poster_uri="https://movies.com",
            release_year=datetime.date(1994, 1, 1),
            title=assembly_title,
        )
        ensemble = Movie.objects.get(title=self.ensemble_title)
        assembly = Movie.objects.get(title=assembly_title)
        self.assertEqual(
            str(ensemble),
            f"{self.ensemble_title} {ensemble.release_year.strftime('%Y')}",
        )
        self.assertEqual(
            str(assembly), f"{assembly.title} {assembly.release_year.strftime('%Y')}"
        )

    def test_review_admin_str_is_title_date(self):
        """Should return a str as ``[movie title] [review date]`` (i.e ``The Matrix 2022-01-12``).
        yyyy-mm-dd format"""
        Review.objects.create(
            movie=Movie.objects.get(title=self.ensemble_title),
            rating=True,
            date=datetime.date(2022, 1, 14),
        )
