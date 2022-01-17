import itertools
import string
import requests
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from movies.models import Movie


class Command(BaseCommand):
    """Command to fetch movie data from the OMDB API.

    Attributes
    ----------
    help : str
        Command line help string for command.
    """

    help = "Gets movie data from OMDB"

    def handle(self, *args, **options):
        """Queries the OMDB API for movie data and stores it in the database.

        Remarks
        -------

            Given the requirement to support CRUD ops on movies and have a db,
            we assume the OMDB API is just a convenient data source, not
            something to target when the app is running.

            OMDB API tends to turn too many results errors for title searches
            with less than three characters. So instead we have to search a
            bit at a time.

            For the purpose of this assessment, there is really is no point in
            taking everything possible. So for each search term, we limit the
            number of saved results to maxResults. This gives data to work with.

            The OMDB API does not accept regex for searches, so there is no way
            to cut the searches down by only requesting matches to the start of
            titles. This means we will get duplicates. So we check the database
            before each insert.

            This command is only meant to populate an assignment database one time.
            If I was seeding or updating a production database there would be a
             lot of cleaning, validating, and error handling to add. We would also
             have to check duplicate entries for updates, reconcile conflicts, and
             deal with things like movies that were deleted in the database but come
             up again in the new upload.
        """
        totalCount = 0
        searches = []

        # Generate search strings.
        alphabets = []
        for letter in string.ascii_lowercase:
            alphabets.append(letter)
        product = itertools.product(alphabets, repeat=3)
        for word in product:
            searches.append(word)

        # Run the searches
        limitResults = True
        maxResults = 5
        for search in searches:
            response = requests.get(
                f"http://www.omdbapi.com/?s={search}&type=movie&page=1&apikey=6ffd0873"
            )
            movie_data = response.json()
            if movie_data["Response"] == "False":
                continue

            totalSearchResults = int(movie_data["totalResults"])
            count = 1
            page = 1
            ids = []
            match = 0
            while True:
                # Get all ids for search
                response = requests.get(
                    f"http://www.omdbapi.com/?s={search}&type=movie&page={page}&apikey=6ffd0873"
                )
                movie_data = response.json()
                if count > totalSearchResults or limitResults and match > maxResults:
                    break
                try:
                    for movie in movie_data["Search"]:
                        ids.append(movie["imdbID"])
                        match += 1

                except KeyError:
                    break

                count += 1
                totalCount += 1
                page += 1

            # Add data for each movie ID
            for id in ids:
                response = requests.get(
                    f"http://www.omdbapi.com/?i={id}&apikey=6ffd0873"
                )
                data = response.json()
                runtime = 0
                if data["Runtime"] == "N/A":
                    runtime = 0
                else:
                    num_filter = filter(str.isdigit, data["Runtime"])
                    runtime = int("".join(num_filter))
                try:
                    Movie.objects.get(title=data["Title"])
                except:
                    Movie.objects.create(
                        description=data["Plot"],
                        duration=runtime,
                        poster_uri=data["Poster"],
                        release_year=f"{data['Year']}-01-01",
                        title=data["Title"],
                    )

        print(Movie.objects.all().count())
