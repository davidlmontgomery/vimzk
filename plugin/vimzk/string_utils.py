"""
String utilities.

"""
import random
import string


def base_n_str_from_number(number, base, digits='0123456789abcdefghijklmnopqrstuvwxyz'):
    """
    Express the value of 'number' as a string in base 'base'.

    Based on http://code.activestate.com/recipes/65212/ (sebastianjb).

    """
    if base < 2 or base > len(digits):
        raise ValueError('base_n_str_from_number: base must be between 2 and len(digits)')

    if number == 0:
        return '0'
    if number < 0:
        sign = '-'
        number = -number
    else:
        sign = ''

    result = ''
    while number:
        result = digits[number % base] + result
        number //= base
    return sign + result


def random_lc_alphanumeric_string(length):
    """Return random lowercase alphanumeric string of specified length."""
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for ii in range(length))
