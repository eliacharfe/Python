import time
from typing import IO


def build_list_of_words(text_file: IO[str]):
    """
    Build a list of words from a file given
    :param text_file: The file containing words
    :return: A list of the words
    """
    return [word for word in text_file]


def build_set_of_words(text_file: IO[str]):
    """
    Build a set of words from a file given
    :param text_file: The file containing words
    :return: A set of the words
    """
    return {word for word in text_file}


def average_runtime(data_structure, word: str):
    """
    Gets a data-structure and a word, and search the word a 1000 times while calculating the time that it tooks
    and returns the time
    :param data_structure: The data structure (must be iterable) to search inside
    :param word: A word to search in the data-structure (1000 times)
    :return: The time took to do the mission
    """
    start_time = time.time()
    for i in range(0, 1000):
        if word in data_structure:
            continue
    return time.time() - start_time


def is_in_set(country: str, line_keyboard: set):
    return set(country).intersection(line_keyboard)


def find_special_state(text_file: IO[str]):
    """
    Find the state that all of its characters are in one line in a regular keyboard
    :param text_file: A text file including names of countries in USA
    :return: The name of the country that we can write in one line in the keyboard
    """
    my_set1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '\n'}
    my_set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', '\n'}
    my_set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm', '\n'}

    for my_set_line in [my_set1, my_set2, my_set3]:
        for country in text_file:
            if is_in_set(country, my_set_line):
                return country
        text_file.seek(0)


if __name__ == '__main__':
    long_words_file = open("resources/words.txt")
    my_list = build_list_of_words(long_words_file)
    my_set = build_set_of_words(long_words_file)
    print(f"time of search in list: {average_runtime(my_list, 'zwitterion')}")
    print(f"time of search in set: {average_runtime(my_set, 'zwitterion')}")
    long_words_file.close()

    my_text_file = open("resources/states.txt")
    print(find_special_state(my_text_file))
