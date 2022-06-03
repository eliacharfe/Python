import numpy as np


def sort_by_axis(square_matrix, axis=0):
    """
    Get an array of a form of a square matrix with values and sort according to the axis sent 0 or 1.
    0 = the “first” axis - vertically (rows).
    1 = the “second” axis - horizontally (cols).
    :param square_matrix: The square matrix.
    :param axis: The axis.
    :return: A square matrix sorted by the axis sent.
    """
    return np.sort(square_matrix, axis=axis)


if __name__ == '__main__':
    arr = np.arange(4, 0, -1).reshape(2, 2)
    print(arr)

    print(sort_by_axis(arr))
    print(sort_by_axis(arr, 1))


