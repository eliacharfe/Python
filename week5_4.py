import itertools
import os
import re
from bs4 import BeautifulSoup


def interleave(*args):
    """
    Take an unlimited list of arguments that can be iterate and returns a list of the elements in order
    for example:
    Input: 'abc', [1, 2, 3], ('!', '@', '#')
    Output: ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
    :param args: An iterable
    :return: A list of elements mixed in order
    """
    return list(sum([elem for elem in zip(*args)], ()))


def interleave_generator(*args):
    """
    Take an unlimited list of arguments that can be iterate and returns a list of the elements in order
    using generator
    for example:
    Input: 'abc', [1, 2, 3], ('!', '@', '#')
    Output: ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
      :param args: An iterable
    :return: A list of elements mixed in order
    """
    for elem in zip(*args):
        yield elem


my_list = []
my_list += [item for element in interleave_generator('abc', [1, 2, 3], ('!', '@', '#'))
            for item in itertools.chain(element)]


def generate_num_chapter_with_titles():
    """
    A generator function that pass on all unordered html files in directory "potter" and for each
    html file extract from the title the number og chapter and the correct new file name to be rename
    this file.
    For example: for the file 1.html that inside of it has the chapter:
                Chapter 81: Taboo Tradeoffs, Pt 3,
                but the correct chapter of 1 is:  A Day of Very Low Probability
                the name of the file will be rename to:  1 A Day of Very Low Probability.html
                and 81.html will be rename to: 81 Taboo Tradeoffs, Pt 3.html
    :return: yield num of chapter and new file name
    """
    for filename in os.listdir("resources/potter"):
        with open("resources/potter/" + filename, "r", encoding="UTF8") as file:
            html_file = BeautifulSoup(file, 'html.parser')
            title = html_file.find('title')
            new_string = title.get_text().replace("Harry Potter and the Methods of Rationality, Chapter", "")
            num_of_chapter = new_string.split()[0][:-1]
            new_file_name = re.sub('[:]', '', new_string)
            yield num_of_chapter, new_file_name


def get_dictionary_of_num_chapter_new_filename():
    return {num_chapter: new_name_file for num_chapter, new_name_file in generate_num_chapter_with_titles()}


def change_files_name():
    """
    Call a function that generate all number of chapters with their correct title names of
    chapter, and build a dictionary that the keys are a the number of chapter and the values
    are the correct name of file that includes the number of chapter and the title, then rename
    all the .html files to their correct names
    :return: None
    """
    num_chapter_filename_dictionary = get_dictionary_of_num_chapter_new_filename()

    for filename_html in os.listdir("resources/potter"):
        for num_of_chapter, new_file_name in num_chapter_filename_dictionary.items():
            if num_of_chapter == re.sub('[.html]', '', filename_html):
                os.rename("resources/potter/" + filename_html, "resources/potter/" + new_file_name + '.html')


if __name__ == '__main__':
    print(f"Regular version: { interleave('abc', [1, 2, 3], ('!', '@', '#')) }")
    print(f"Generator version: { my_list }")

    change_files_name()


