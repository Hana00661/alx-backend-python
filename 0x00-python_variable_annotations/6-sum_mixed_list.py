#!/usr/bin/env python3
"""Module for task 6
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Type-annotated function which takes a list mxd_lst of integers
    and floats and returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The list of integers and
        floats to sum.

    Returns:
        float: The sum of the elements in the list.
    """
    return float(sum(mxd_lst))
