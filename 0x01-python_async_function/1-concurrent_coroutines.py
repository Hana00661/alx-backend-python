#!/usr/bin/env python3
"""1-concurrent_coroutines.py
"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Async routine that spawns wait_random n times.

    Args:
        n (int): The number of times to wait.
        max_delay (int): The maximum delay

    Returns:
        List[float]: list of all the delays.
    """
    wait_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)
