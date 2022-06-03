import numpy as np
from numpy.typing import NDArray


def convert_two_1d_arrays_into_one_2d_array(first_array: NDArray, second_array: NDArray) -> NDArray:
    """
    Get two 1-D arrays of same size and convert n sequence depth wise) them into one 2-D arrays of
    element-by-element.
    https://numpy.org/doc/stable/reference/generated/numpy.dstack.html
    :param first_array: A 1-D array.
    :param second_array: A 1-D array.
    :return: A 2-D array.
    """
    return np.dstack((first_array, second_array))


if __name__ == '__main__':
    array1 = np.array((1, 2, 3, 4))
    array2 = np.array((2, 3, 4, 5))

    print(convert_two_1d_arrays_into_one_2d_array(array1, array2))


