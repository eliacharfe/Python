from typing import List


def full_names(firsts_names: List[str], lasts_names: List[str], min_length: int = 0) -> List[str]:
    """
    Gets a list of first names and a list of last names and an optional parameter min_length and return
    a list of all combinations of first names with last names that are greater or equal to the min_length
    if passed (by default min_length is 0), that after will turn each first/last name to uppercase at
    the first letter.
    :param firsts_names: A list of first names.
    :param lasts_names: A list of last names.
    :param min_length: (optional) The full names that are greater than this parameter.
    :return: List of all full names.
    """
    return [first.capitalize() + " " + last.capitalize()
            for first in firsts_names for last in lasts_names
            if len(first + ' ' + last) >= min_length]


if __name__ == '__main__':
    first_names = ['avi', 'moshe', 'yaakov']
    last_names = ['cohen', 'levi', 'mizrahi']

    print(full_names(first_names, last_names))
    print(full_names(first_names, last_names, 10))

