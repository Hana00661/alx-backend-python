#!/usr/bin/env python3
"""0-basic_async_syntax.py
"""


import asyncio, random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that waits for a random delay between 0 and
    max_delay.

    Args:
        max_delay (int, optional): defaults to 10.

    Returns:
        float: The delay in seconds.
    """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
