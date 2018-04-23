"""
Routines for working with zettel ids (zids).

"""
from datetime import date

from vimzk.string_utils import base_n_str_from_number, random_lc_alphanumeric_string


ZK_START_DATE = date(2018, 4, 18)
_PREFIX_LENGTH = 5
_DATE_LENGTH = 3
ZID_LENGTH = _PREFIX_LENGTH + _DATE_LENGTH


def create_zid(zid_date=date.today()):
    """
    Return a new zettel id (zid).

    A zid consists of 5 random alphanumeric chars followed
    by the last 3 chars of a base-36 encoding of the date
    as the number of days since ZK_START_DATE. (This'll
    wrap after about 128 years. I think that'll be ok.)

    The intention is for a zid to be unique (in practice),
    short, and encode the date.

    """
    prefix = random_lc_alphanumeric_string(_PREFIX_LENGTH)
    day_number = (zid_date - ZK_START_DATE).days
    date_string = base_n_str_from_number(day_number, 36)
    if date_string[0] == '-':
        date_string = date_string[1:]
    date_string = date_string.rjust(_DATE_LENGTH, '0')[-3:]
    return prefix + date_string
