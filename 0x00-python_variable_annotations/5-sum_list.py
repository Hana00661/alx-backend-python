#!/usr/bin/env python3
"""Module for task 5
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Type-annotated function which takes a list input_list of floats as
    argument and returns their sum as a float.

    Args:
        input_list (List[float]): list of floats to sum.

    Returns:
        float: The sum of the elements in the list.
    """
    return float(sum(input_list))
