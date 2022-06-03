from typing import Callable, Iterable, Iterator


def my_filter(function: Callable[[], any], iterable: Iterable[any]) -> Iterator:
    """
    Implementation of the function "filter" of python.
    :param function: A function.
    :param iterable: An iterable.
    :return: All items in the iterable sent that the function returns true when gets those items.
    """
    for item in iterable:
        if function(item):
            yield item


if __name__ == '__main__':
    for polyndrome in my_filter(lambda word: word == word[::-1],
                                ['abba', 'bob', 'week6_2', '1234', 'python', 'ArqqrA', 'WoW']):
        print(polyndrome)



