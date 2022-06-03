from typing import List

import numpy as np
from numpy.typing import NDArray


def create_student_ids(id_list: List[int]) -> NDArray:
    return np.array(id_list)


def create_students_height(height_list: List[float]) -> NDArray:
    return np.array(height_list)


def create_indices_sorted_by_primary_key(primary_key_array: NDArray, secondary_key_array: NDArray) -> NDArray:
    """
    Get 2 arrays and return an array of integer indices representing the sorting order by "primary_key_array"
    parameter and then by "secondary_key_array".
        For example:
        array of primary key is : [10, 3, 10]
        array of secondary key is : [5, 3, 4]
        output: [1, 2, 0]
    :param primary_key_array:
    :param secondary_key_array:
    :return:
    """
    return np.lexsort((secondary_key_array, primary_key_array))


def print_indices_describing_sort_order_by_multiple_columns_and_sorted_data():
    """
    Print the integer indices that describes the sort order by multiple columns and the sorted data.
    Inspired from: https://www.w3resource.com/python-exercises/numpy/python-numpy-sorting-and-searching-exercise-4.php
    """
    student_id = create_student_ids([1023, 5202, 6230, 1671, 1682, 5241, 4532])
    student_height = create_students_height([40., 42., 45., 41., 38., 40., 42.0])

    indices = create_indices_sorted_by_primary_key(student_height, student_id)

    print("Sorted indices:")
    print(indices)

    print("Sorted data:")
    for i in indices:
        print(student_id[i], student_height[i])


if __name__ == '__main__':
    print_indices_describing_sort_order_by_multiple_columns_and_sorted_data()