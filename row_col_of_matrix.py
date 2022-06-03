import numpy as np


def find_num_of_row_col_in_matrix(matrix: np.ndarray) -> tuple:
    """
    Get a matrix and return a tuple of 2 elements which the first one is the number of rows and
    the second is the number of columns.
    :param matrix: A matrix.
    :return: A tuple.
    """
    return matrix.shape


if __name__ == '__main__':
    arr = np.arange(0, 20, 1)

    my_matrix = arr.reshape((5, 4))
    (row, col) = find_num_of_row_col_in_matrix(my_matrix)
    print(f"num row: {str(row)}\n"
          f"num col: {str(col)}\n")

    my_matrix = arr.reshape((2, 10))
    (row, col) = find_num_of_row_col_in_matrix(my_matrix)
    print(f"num row: {str(row)}\n"
          f"num col: {str(col)}\n")

