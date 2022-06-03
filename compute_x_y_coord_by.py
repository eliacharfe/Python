import numpy as np
import matplotlib.pyplot as pyplot
from numpy.typing import NDArray
from typing import Tuple


def compute_x_y_coordinates_of_sine_curve(start: float, end: float, step: float, dtype: type)\
        -> Tuple[NDArray, NDArray]:
    """
    Get a range of x coordinates (start to end with a step parameter) and return a tuple which
    the first element is an array of this x range coordinates and the second element if the
    computation of the sine of this range.
    :param start: Start value of sequence.
    :param end: Final value of sequence.
    :param step: The step between the values.
    :param dtype: The type of the values.
    :return: A tuple like explained.
    """
    x_coordinates_range = np.arange(start, end, step, dtype=dtype)
    sine_of_range_x = np.sin(x_coordinates_range)
    return x_coordinates_range, sine_of_range_x


def show_result_sine_curve_at_range(start: float, end: float, step: float, dtype: type)\
        -> None:
    """
    Get a range of x coordinates (start to end with a step parameter) and compute the x range coordinates
    and the sine of this range. Then uses matplotlib to plot it to the screen and show it as a graph
    :param start: Start value of sequence.
    :param end: Final value of sequence.
    :param step: The step between the values.
    :param dtype: The type of the values.
    """
    (x_range_coord, sin_of_range_x) = compute_x_y_coordinates_of_sine_curve(start, end, step, dtype)
    pyplot.plot(x_range_coord, sin_of_range_x)
    pyplot.show()


if __name__ == '__main__':

    show_result_sine_curve_at_range(-5, 5, 0.1, float)


