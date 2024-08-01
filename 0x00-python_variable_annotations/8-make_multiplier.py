#!/usr/bin/env python3
"""Module for task 8
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Type-annotated function that takes a float multiplier as argument

    Args:
        multiplier (float): The float to use as the multiplier.

    Returns:
        Callable[[float], float]: A function that multiplies a float by
        the multiplier.
    """
    return lambda x: x * multiplier
