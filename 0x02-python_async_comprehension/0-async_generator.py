#!/usr/bin/env python3

"""0-async_generator.py
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Coroutine that generates random numbers between 0 and 10, one number
    at a time.

    yields: a random number bewteen 0 and 10
            then waits asynchronously for a second
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
