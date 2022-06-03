import numpy as np
from numpy.typing import NDArray


def create_matrix_with_borders_ones_and_inside_zeros() -> NDArray:
    """
    Create a matrix of 10x10 in which the elements on the borders will be equal to 1, and inside 0.
    :return: The matrix.
    """
    matrix = np.ones((10, 10))
    matrix[1:9, 1:9] = 0
    return matrix


if __name__ == '__main__':
    print(create_matrix_with_borders_ones_and_inside_zeros())


