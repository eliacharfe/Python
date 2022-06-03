import numpy as np
from datetime import datetime


def find_number_days_between_2_dates(first_date: str, second_date: str) -> np.timedelta64:
    """
    Get 2 dates and return number of days between them (if valid dates).
    :param first_date: The first date.
    :param second_date: The second date.
    :return: How many days between.
    """
    try:
        datetime.strptime(first_date, '%Y-%m-%d')
        datetime.strptime(second_date, '%Y-%m-%d')
        if first_date > second_date:
            raise ValueError("The first date should be before the second date")
        return np.datetime64(second_date) - np.datetime64(first_date)
    except (UnboundLocalError, ValueError, TypeError) as e:
        print(e)


if __name__ == '__main__':
    num_days = find_number_days_between_2_dates('2022-04-01', '2022-05-01')
    if num_days:
        print(num_days)

