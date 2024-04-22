#!/usr/bin/env python3
'''
Import wait_random from the previous python file
New async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay
Will spawn wait_random n times with the specified max_delay.
Returns the list of all the delays (float values),
in ascending order without using sort()
'''


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    takes 2 ints
    returns a list of floats
    '''
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    list_delays = []
    for task in asyncio.as_completed(tasks):
        list_delays.append(await task)
    return list_delays
