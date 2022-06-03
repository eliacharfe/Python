import numpy as np
from numpy.typing import NDArray


def compute_median_array(array: NDArray) -> float:
    """
    Get an array and return its median value.
    :param array: The array to compute its median.
    :return: The median (float) of the array.
    """
    return np.median(array)


def create_random_array_and_compute_its_median(low, high, shape, dtype):
    """
    Create a randomized values array at the range given (low to high) according to the shape and type passed
    and compute the median's array.
    :param low: The lower number of the sequence.
    :param high: The higher number of the sequence.
    :param shape: The shape of the array.
    :param dtype: The type of the values randomized.
    :return: The median (float) of the array.
    """
    arr = np.random.randint(low=low, high=high, size=shape, dtype=dtype)
    return compute_median_array(arr)


if __name__ == '__main__':
    print(create_random_array_and_compute_its_median(0, 10, (2, 6), dtype=int))




