"""
Utility functions and error classes used throughout client classes
"""
import datetime
import math
import six


class CongressError(Exception):
    """
    Exception for general Congress API errors
    """
    def __init__(self, message, response=None, url=None):
        super(CongressError, self).__init__(message)
        self.message = message
        self.response = response
        self.url = url


class NotFound(CongressError):
    """
    Exception for things not found
    """


def check_chamber(chamber):
    "Validate that chamber is house or senate or both or joint"
    if str(chamber).lower() not in ('house', 'senate', 'both', 'joint'):
        raise TypeError('chamber must be either "house" or "senate" or "both" or "joint"')


def check_category(category):
    """
    Validate that category is travel, personnel, rent-utilities, 
    other-services, supplies, franked-mail, printing, equipment, total
    """
    if str(category).lower() not in ('travel', 'personnel', 'rent-utilities', 
    'other-services', 'supplies', 'franked-mail', 'printing', 'equipment', 'total'):
        raise TypeError('Category must be an approved category, check docs')


def check_comms(category):
    """
    Validate that category is ec, pm, or pom
    """
    if str(category).lower() not in ('ec', 'pm', 'pom'):
        raise TypeError('Communications Category must be an approved category, check docs')


def check_quarter(quarter):
    "Validate that quarter is 1, 2, 3, or 4"
    if str(quarter) not in ('1', '2', '3', '4'):
        raise TypeError('Quarter must be either 1, 2, 3, or 4')


def get_congress(year):
    "Return the Congress number for a given year"
    if year < 1789:
        raise CongressError('There was no Congress before 1789.')

    return int(math.floor((year - 1789) / 2 + 1))


def get_offset(page):
    if page < 1:
        raise CongressError('Page number must be at least 1.')
    return (page - 1) * 20
    

def parse_date(s):
    """
    Parse a date using dateutil.parser.parse if available,
    falling back to datetime.datetime.strptime if not
    """
    if isinstance(s, (datetime.datetime, datetime.date)):
        return s
    try:
        from dateutil.parser import parse
    except ImportError:
        parse = lambda d: datetime.datetime.strptime(d, "%Y-%m-%d")
    return parse(s)


def u(text, encoding='utf-8'):
    "Return unicode text, no matter what"

    if isinstance(text, six.binary_type):
        text = text.decode(encoding)

    # it's already unicode
    text = text.replace('\r\n', '\n')
    return text


CURRENT_CONGRESS = get_congress(datetime.datetime.now().year)
