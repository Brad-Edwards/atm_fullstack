import datetime

from dateutil.relativedelta import relativedelta

MIN_DURATION = 1
MIN_RELEASE_YEAR = 1900
MAX_RELEASE_YEAR = (datetime.date.today() + relativedelta(years=10)).year


def validate_release_year(year):
    """Checks that release for a movie is between the minimum and maximum
    allowed years.

    Parameters
    ----------
    year : int
        The release year to validate.

    Returns
    -------
    bool
        True if the year is valid, otherwise false.
    """
    return MIN_RELEASE_YEAR < year < MAX_RELEASE_YEAR
