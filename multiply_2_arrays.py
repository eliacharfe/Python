import numpy as np
from numpy.typing import NDArray


def multiply_2_same_sized_array_each_elements_corresponding(first_array: NDArray, second_array: NDArray) -> NDArray:
    """
    Get 2 same sized arrays and multiply element-by-element and return a new array of the result.
    :param first_array: First array.
    :param second_array: Second array.
    :return: An array.
    """
    return np.multiply(first_array, second_array)


if __name__ == '__main__':
    array1 = np.array([1, 2, 3, 4])
    array2 = np.array([10, 5, 3, 2])

    print(multiply_2_same_sized_array_each_elements_corresponding(array1 , array2))


