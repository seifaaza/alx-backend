#!/usr/bin/env python3
"""
Defines a function named `index_range`
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates start end index from list of pagination parameters.
    Args:
        page (int): the current page
        page_size (int): the amount of items in a page
    Returns:
        (tuple): a tuple of start end index for given page
    """
    NxtPgIdx = page * page_size
    return NxtPgIdx - page_size, NxtPgIdx
