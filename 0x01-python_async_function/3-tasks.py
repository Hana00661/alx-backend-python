#!/usr/bin/env python3
""" 3-tasks.py
"""


import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Function that takes an integer max_delay and returns a asyncio.Task.

    Args:
        max_delay (int): The maximum delay.

    Returns:
        asyncio.Task: A asynchronously waits for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))
