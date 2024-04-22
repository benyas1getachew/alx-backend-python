#!/usr/bin/env python3
'''
From the previous file, import wait_n into 2-measure_runtime.py.
Create a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay),
returns total_time / n (float)
'''


import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    takes 2 ints
    returns a float
    '''
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time() - start
    return end / n
