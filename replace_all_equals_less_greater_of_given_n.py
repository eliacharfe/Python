import numpy as np
import operator
from numpy.typing import NDArray

__dict_operators = {'<': operator.lt, "==": operator.eq, '>': operator.gt}


def replace_all_less_equal_or_greater_than_num_in_array(
        array: NDArray, num: float, value_of_replace: float = 0, compare_operator='==') -> NDArray:
    """
    Replace all numbers in a given array which is less/equal/greater to a given number with a value passed
    according to the operator passed.
    :param array: The original array.
    :param num: The number in which all numbers need to be compared to.
    :param value_of_replace: The value to insert instead of the elements that are < / == / > the number
    according to the operator passed.
    :param compare_operator: The comparison operator.
    :return: The new array replaced.
    """
    return np.where(__dict_operators[compare_operator](array, num), value_of_replace, array)


if __name__ == '__main__':
    arr = np.array([2, 8, 20, 4, 11])
    n = 8

    arr_less_replaced = replace_all_less_equal_or_greater_than_num_in_array(arr, n, -1, '<')
    print(arr_less_replaced)

    arr_eq_replaced = replace_all_less_equal_or_greater_than_num_in_array(arr, n, -1, '==')
    print(arr_eq_replaced)

    arr_greater_replaced = replace_all_less_equal_or_greater_than_num_in_array(arr, n, -1, '>')
    print(arr_greater_replaced)


