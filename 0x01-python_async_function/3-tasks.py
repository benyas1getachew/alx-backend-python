#!/usr/bin/env python3
'''
Import wait_random from 0-basic_async_syntax.
Regular function task_wait_random that takes an integer max_delay
returns a asyncio.Task.
'''

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    takes an int
    returns asyncio.Task
    '''
    return asyncio.create_task(wait_random(max_delay))
