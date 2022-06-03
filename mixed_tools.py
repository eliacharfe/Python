import itertools
from typing import List, Iterator


def interleave(*args) -> List[any]:
    """
    Take an unlimited list of arguments that can be iterate and returns a list of the elements in order
    for example:
    Input: 'abc', [1, 2, 3], ('!', '@', '#')
    Output: ['a', 1, '!', 'b', 2, '@', 'c', 3, '#']
    :param args: An iterable
    :return: A list of elements mixed in order
    """
    return list(sum([elem for elem in zip(*args)], ()))


def interleave_generator(*args) -> Iterator[any]:
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


if __name__ == '__main__':
    print(f"Regular version: {interleave('abc', [1, 2, 3], ('!', '@', '#'))}")

    my_list = []
    my_list += [item for element in interleave_generator('abc', [1, 2, 3], ('!', '@', '#'))
                for item in itertools.chain(element)]
    print(f"Generator version: {my_list}")

