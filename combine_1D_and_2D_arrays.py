import numpy as np
from typing import Iterator

from numpy.typing import NDArray


def generate_combination_1d_and_2d_arrays(array_1d: NDArray, array_2d: NDArray) -> Iterator:
    """
    Get 1D array and 2D array and return an iterator to a combination of the 2 of them.
    :param array_1d: A 1-D array.
    :param array_2d: A 2-D array.
    :return: Iterator.
    """
    return np.nditer([array_1d, array_2d])


def create_1d_2d_arrays_combine_them_display_elements() -> None:
    """
    Create 1D array and 2D array combine them then display the elements of the combination.
    """
    arr_1d = np.arange(4)
    arr_2d = np.arange(8).reshape(2, 4)

    for elem_1D, elem_2D in generate_combination_1d_and_2d_arrays(arr_1d, arr_2d):
        print(f"elem 1D: {elem_1D}, elem 2D: {elem_2D}")


if __name__ == '__main__':
    create_1d_2d_arrays_combine_them_display_elements()


