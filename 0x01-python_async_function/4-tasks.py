#!/usr/bin/env python3
"""4-tasks.py
"""


import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """coroutine take the code from wait_n and alter it into new function.

    Args:
        n (int): The number of tasks to create.
        max_delay (int): The maximum delay to wait for.

    Returns:
        List[float]: A list of asyncio.Task objects that asynchronously
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
