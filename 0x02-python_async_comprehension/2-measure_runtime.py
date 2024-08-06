#!/usr/bin/env python3
"""2-measure_runtime.py
"""


import asyncio
from time import perf_counter


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """a coroutine that measures the total runtime async_comprehension

    Return: the total runtime of the async_comprehension
    """

    start_time = perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    return perf_counter() - start_time
