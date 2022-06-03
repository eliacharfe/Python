import numpy as np


def remove_single_dimensional_entries(array):
    """
    Get an array and remove single-dimensional entries from its shape.
    Found solution here: https://www.geeksforgeeks.org/numpy-squeeze-in-python/
    :param array: An array to remove from.
    :return: An array.
    """
    return np.squeeze(array)


if __name__ == '__main__':
    arr = np.array([[[2, 2, 2], [2, 2, 2]]])
    print(arr.shape)

    arr_removed_single_entries = remove_single_dimensional_entries(arr)
    print(arr_removed_single_entries.shape)




