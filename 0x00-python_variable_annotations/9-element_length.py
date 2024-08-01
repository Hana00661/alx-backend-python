#!/usr/bin/env python3
"""Module for task 9
"""

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Creates a list of tuples, where each tuple contains a string.

    Args:
        lst (List[str]): The list of strings to process.

    Returns:
         List[Tuple[str, int]]: A list of tuples, where each tuple contains
         a string.
    """
    return [(i, len(i)) for i in lst]
