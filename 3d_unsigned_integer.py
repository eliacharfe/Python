import numpy as np


def create_3d_array_of_a_shape_fill_with_certain_type_in_a_range(
        low_range, high_range, num_of_matrices, num_rows, num_columns, dtype):
    """
    Create a three-dimension array with shape (num_of_matrices, num_rows, num_columns) and fill the array
    elements with random values at range low_range to high_range according to the type passed.
    :param low_range: Lower element of the range.
    :param high_range: Highest element of the range.
    :param num_of_matrices: The number of matrices.
    :param num_rows: The number of rows (for each matrix).
    :param num_columns: The number of columns (for each matrix).
    :param dtype: The type of values to random.
    :return: An array like explained.
    """
    shape = (num_of_matrices, num_rows, num_columns)
    arr = np.random.randint(low=low_range, high=high_range, size=shape, dtype=dtype)
    return arr


if __name__ == '__main__':
    print(create_3d_array_of_a_shape_fill_with_certain_type_in_a_range(0, 255, 300, 400, 5, np.uint))


