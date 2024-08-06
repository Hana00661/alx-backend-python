#!/usr/bin/env python3
"""2-measure_runtime.py
"""


import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """a function that measures the total execution time.

    Args:
        n : The number of times to wait.
        max_delay : The maximum delay to wait for.

    Returns:
        float: The average time taken to execute.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return (total_time) / n
