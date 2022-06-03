import numpy as np
from numpy.typing import NDArray


def create_square_matrix_random_values_of_size(size=4) -> NDArray:
    """
    Create a square matrix of size given and initiate random values inside and return the matrix.
    :param size: Number of rows/columns.
    :return: An numpy array.
    """
    return np.random.rand(size, size)


def duplicate_matrix_and_swap_2_give_rows(original_matrix: NDArray, first_index_row: int, second_index_row: int)\
        -> NDArray:
    """
    Get a matrix and duplicate it to a new matrix, the swap 2 rows according to the 2 the indexes parameters
    passed and return the new matrix.
    :param original_matrix: The original matrix.
    :param first_index_row: The index of the first row to swap.
    :param second_index_row: The index of the second row to swap.
    :return: A numpy array.
    """
    matrix_dup = np.copy(original_matrix)
    matrix_dup[first_index_row] = original_matrix[second_index_row]
    matrix_dup[second_index_row] = original_matrix[first_index_row]
    return matrix_dup


if __name__ == '__main__':
    matrix = create_square_matrix_random_values_of_size(4)
    print(matrix)

    last_row_index = matrix.shape[0] - 1
    new_dup_matrix_swapped = duplicate_matrix_and_swap_2_give_rows(matrix, 0, last_row_index)
    print("Duplicated matrix swapped 2 rows (first, last):")
    print(new_dup_matrix_swapped)

