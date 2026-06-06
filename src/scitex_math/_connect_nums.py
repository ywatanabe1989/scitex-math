#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: "2024-11-02 12:50:29 (ywatanabe)"
# File: ./src/scitex_math/_connect_nums.py
"""Connect numbers/values with hyphens.

Ported from scitex_gen.misc.connect_nums (Phase B retirement wave).
"""

from __future__ import annotations


def connect_nums(nums):
    """Connect multiple numbers/values with hyphens.

    This function takes an iterable of numbers or values and joins them
    with hyphens to create a single string representation.

    Parameters
    ----------
    nums : iterable
        An iterable of numbers or values to be connected.

    Returns
    -------
    str
        A string with the values joined by hyphens.

    Example
    -------
    >>> connect_nums((0, 0))
    '0-0'
    >>> connect_nums((1, 2, 3))
    '1-2-3'
    >>> connect_nums(('a', 'b'))
    'a-b'
    """
    return "-".join(str(num) for num in nums)


# EOF
