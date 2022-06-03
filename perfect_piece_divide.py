from functools import reduce
from typing import Iterator
from itertools import count as infinite_count


def generate_all_perfect_dividers(start_divider: int = 2) -> Iterator[int]:
    """
    Generator that generates all positive integers greater(or equals) to the integer passed to
    the function, that the sum of their divisors are equals to them ("perfect dividers").
    :param start_divider: The start integer.
    :return: An iterator of the "perfect dividers".
    """
    for divider in infinite_count(start_divider):
        all_divisors_of_divider = filter(lambda num: divider % num == 0, range(1, divider // 2 + 1))
        if divider == reduce(lambda total, new_div: total + new_div, all_divisors_of_divider):
            yield divider


def print_all_dividers_equals_to_sum_of_their_divisors() -> None:
    """
    Print all positive integers that the sum of their divisors are equals to them.
    """
    for perfect_divider in generate_all_perfect_dividers(6):
        print(perfect_divider)


if __name__ == '__main__':
    print_all_dividers_equals_to_sum_of_their_divisors()

