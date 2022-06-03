import numpy as np
from numpy.typing import NDArray


def create_matrix(*args: list) -> NDArray[[int]]:
    """
    Get a list of lists and return a matrix.
    :param args: List of list which the values are the same type.
    :return: A matrix.
    """
    return np.array(args)


def create_vector(lst: list) -> NDArray[int]:
    """
    Create a vector from a list.
    :param lst:
    :return: A vector.
    """
    return np.array(lst)


def add_vector_to_matrix(matrix: NDArray[[int]], vector: NDArray[int]) -> NDArray[[int]]:
    """
    Get a matrix and a vector and add the vector to each row of the given matrix.
    :param matrix: A matrix.
    :param vector: A vector.
    :return: A new matrix.
    """
    return matrix + vector


if __name__ == '__main__':
    my_matrix = create_matrix([[0, 1, 0], [4, 4, 4], [-1, 0, -1]])
    my_vector = create_vector([1, -1, 1])

    print(add_vector_to_matrix(my_matrix, my_vector))




