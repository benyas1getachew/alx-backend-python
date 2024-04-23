#!/usr/bin/env python3
"""
coroutine called async_comprehension that takes no arguments
"""


import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    coroutine will collect 10 random numbers
    using an async comprehensing over async_generator
    then return the 10 random numbers
    """
    x = [i async for i in async_generator()]
    return x
