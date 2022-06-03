import datetime
import os
import random


def find_files_with_deep_prefix(directory_path: str):
    """
    This function gets the path to a directory and return a list of files that start with the string "deep"
    :param directory_path: The path to the directory.
    :return: List of files that start with "deep"
    """
    return [filename for filename in os.listdir(directory_path) if filename.startswith("deep")]


def get_random_date_between(first_date: datetime.date, second_date: datetime.date):
    """
    The function gets 2 dates and return a random date between those dates.
    Taken from the internet.
    """
    random_number_of_days = random.randrange(abs(first_date - second_date).days)
    random_date_between_dates = first_date + datetime.timedelta(random_number_of_days)
    return random_date_between_dates


def random_date_between_dates_check_if_monday(first_input_date, second_input_date):
    """
     The function gets 2 dates and after generate a random number between then print "I dont have
     vinaigrette" if the the random date fall on monday.
    """
    try:
        first_date = datetime.datetime.strptime(first_input_date, "%Y-%m-%d").date()
        second_date = datetime.datetime.strptime(second_input_date, "%Y-%m-%d").date()
    except ValueError:
        return "Wrong format: the correct format is: YYYY-MM-DD"

    random_date = get_random_date_between(first_date, second_date)
    print("Random date between is: " + str(random_date))
    if random_date.isoweekday() == 2:
        print("I dont have vinaigrette")


if __name__ == "__main__":
    print(f"List of files that start with deep: {find_files_with_deep_prefix('images')}")

    random_date_between_dates_check_if_monday(input("Enter a date\n"), input("Enter a second date\n"))


