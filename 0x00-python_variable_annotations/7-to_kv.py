#!/usr/bin/env python3
"""Module for task 7
"""


from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Type-annotated function that takes a string k and an int OR float v
    as arguments and returns a tuple.

    Args:
        k (str): The string to include in the tuple.
        v (Union[int, float]): The integer or float to square

    Returns:
        Tuple[str, float]: The tuple with the string as the first element
    """
    return (k, float(v**2))
