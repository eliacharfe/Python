import numpy as np


def create_numpy_array(start: [int, float], end: [int, float], step: [int, float], dtype: type) -> np.arange:
    """
    Create an array according to the start value passed, the end, and step between each value,
    and put those values according to the type passed, then return the array.
    :param start: Start value.
    :param end: Final value.
    :param step: The step between the values.
    :param dtype: The type of the values in the array.
    :return:
    """
    return np.arange(start, end, step, dtype=dtype)


def change_sign_at_indexes(arr: np.ndarray, start_index: int, end_index: int) -> np.array:
    """
    Get an array and change the sign of the the values at indexes from start_index to end_index
    that were passed.
    :param arr: The array.
    :param start_index: The start index.
    :param end_index: The last index.
    """
    arr[(arr >= start_index) & (arr <= end_index)] *= -1


if __name__ == '__main__':

    my_array = create_numpy_array(0, 20, 1, int)
    change_sign_at_indexes(my_array, 9, 15)

    print(my_array)
