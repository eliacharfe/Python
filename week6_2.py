import operator
import time


def create_dictionary_of_calculation_functions(first_number: float, second_number: float):
    dictionary_of_calculation_functions = {
        '+': operator.add(first_number, second_number),
        '-': operator.sub(first_number, second_number),
        '*': operator.mul(first_number, second_number),
        '/': operator.truediv(first_number, second_number)
    }
    return dictionary_of_calculation_functions


def calc(first_number: float, second_number: float, math_sign):
    """
    Gets 2 numbers and a math sign (+, -, * or /) and return the result by using a dictionary of functions
    :param first_number: First number
    :param second_number: Second number
    :param math_sign: A math sign
    :return:
    """
    return create_dictionary_of_calculation_functions(first_number, second_number)[math_sign]


def apply(func, iterable):
    """
    A generator that gets a function and an iterable and on each item of the iterable return the result
    of the item after activate the function on it
    :param func: A function
    :param iterable: An iterable
    :return: Activation of the function on each item of the iterable
    """
    for item in iterable:
        yield func(item)


# map


def generate_first_names(lst_full_names):
    """
    Generator function that get a list of full names and returns an iterator that point only to the first names
    :param lst_full_names: A list of full names (using map)
    :return: An iterator of the first names only
    """
    return map(lambda name:  name.split(' ', 1)[0], lst_full_names)


# filter


def generate_only_polyndromes(lst_of_words):
    """
    Generator that get list of words and returns a generator of the words that are polyndromes only
    :param lst_of_words: A list of words (using filter)
    :return: An iterator on the words that are polyndromes
    """
    return filter(lambda word: word == word[::-1], lst_of_words)


# Personally adjusted filter


def my_filter(func, iterable):
    """
    A generator function that implement the known function "filter of python
    :param func: A function
    :param iterable: An iterable
    :return: An iterator of the items in the iterable that return True from the function sent
    """
    for item in iterable:
        if func(item):
            yield item


# Stay ? positive


def get_positive_numbers(inp):
    """
    A function that gets an input of numbers seperated by ',' and return a list of the positive numbers
    :param inp: The input from the user
    :return: list of all positives
    """
    return list(filter(lambda x: int(x) > 0, list(map(int, inp.split(",")))))


# 2000 running


def timer(f, *args):
    """
    A function that check out the time that to the function passed to run on the arguments passed
    :param f: A function
    :param args: A list of arguments
    :return: The time that the function passed run on the arguments passed
    """
    start_time = time.time()
    f(args)
    return time.time() - start_time


if __name__ == '__main__':
    print(calc(5, 2, '+'))
    print(calc(5, 2, '-'))
    print(calc(5, 2, '*'))
    print(calc(5, 2, '/'))
    print("-------------------------------------------")

    square_check = apply(lambda number: number ** 2, [5, -1, 6, -8, 0])
    print(tuple(square_check) == (25, 1, 36, 64, 0))
    print("------------------------------------------------")

    for first_name in generate_first_names(['Bob Smith', 'Alice Johnson', 'Ali Baba']):
        print(first_name)
    print("----------------------------------------------")

    for polyndrome in generate_only_polyndromes(['abba', 'bob', 'week6_2', '1234', 'python', 'ArqqrA', 'WoW']):
        print(polyndrome)
    print("---------------------------------------------------")

    closet = [
        {'name': 'Peter', 'year_of_birth': 1927, 'gender': 'Male'},
        {'name': 'Edmund', 'year_of_birth': 1930, 'gender': 'Male'},
        {'name': 'Lucy', 'year_of_birth': 1932, 'gender': 'Female'},
        {'name': 'Susan', 'year_of_birth': 1928, 'gender': 'Female'},
        {'name': 'Jadis', 'year_of_birth': 0, 'gender': 'Female'},
    ]

    print(f"Sorted by the last character of the name: ")
    print('\n'.join(map(str,
                        sorted(closet, key=lambda d: d['name'][-1]))))
    print("---------------------------------------------------")

    for polyndrome in my_filter(lambda word: word == word[::-1],
                                ['abba', 'bob', 'week6_2', '1234', 'python', 'ArqqrA', 'WoW']):
        print(polyndrome)
    print("--------------------------------------------")

    print(get_positive_numbers(input("Enter a serie of numbers separated by ',': \n")))
    print("--------------------------------------------------------")

    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
