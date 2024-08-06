#!/usr/bin/env python3
"""1-async_comprehension.py
"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Coroutine that generates a list of 10 random numbers.

        Return: the 10 random number
    """
    return [num async for num in async_generator()]
