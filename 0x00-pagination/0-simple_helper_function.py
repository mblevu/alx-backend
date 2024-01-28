#!/usr/bin/env python3
"""
simple helper function
"""
from typing import Tuple


def index_range(page, page_size) -> Tuple:
    """
    Returns the start and end indices for a given page and page size.
    """
    start_index = (page - 1) * page_size
    if start_index < 0:
        start_index = 0
    end_index = page * page_size
    return (start_index, end_index)
