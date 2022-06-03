from ctypes import Array

import numpy as np


def evenly_distributed_between(start_value: [int, float], end_value: [int, float], length_of_vec=10) \
        -> np.linspace:
    """
    Create a vector of length of "length_of_vec" parameter with values evenly distributed
    between "start_value" and "stop_value" passed, and return the vector.
    :param start_value: The starting value of the sequence.
    :param end_value: The end value of the sequence.
    :param length_of_vec: Number of samples to generate.
    :return: A vector of length of "length_of_vec" parameter with values evenly distributed
    between "start_value" and "stop_value".
    """
    return np.linspace(start_value, end_value, length_of_vec)


if __name__ == '__main__':

    print(evenly_distributed_between(5, 50, 10))


