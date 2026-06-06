#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""find_closest — find the closest value in a sorted list to a given number.

Ported from scitex-gen `misc.py` as part of the scitex-gen full retirement.
"""
from __future__ import annotations

import math
from bisect import bisect_left

import numpy as np


def find_closest(list_obj, num_insert):
    """Find the closest value in a sorted list to a given number.

    Parameters
    ----------
    list_obj : list or array-like
        A sorted list of numbers.
    num_insert : float or int
        The number to find the closest value to.

    Returns
    -------
    tuple
        A tuple containing (closest_value, index_of_closest_value).

    Notes
    -----
    Assumes ``list_obj`` is sorted. If ``num_insert`` is NaN, both members
    of the tuple are NaN. If duplicate values are present and the target
    sits exactly between them, the lower-indexed element is returned.

    Example
    -------
    >>> find_closest([1, 3, 5, 7, 9], 6)
    (5, 2)
    >>> find_closest([1, 3, 5, 7, 9], 8)
    (7, 3)
    """
    if isinstance(num_insert, float) and math.isnan(num_insert):
        return np.nan, np.nan

    pos_num_insert = bisect_left(list_obj, num_insert)

    if pos_num_insert == 0:
        return list_obj[0], pos_num_insert

    if pos_num_insert == len(list_obj):
        return list_obj[-1], pos_num_insert

    pos_before = pos_num_insert - 1
    before_num = list_obj[pos_before]
    after_num = list_obj[pos_num_insert]

    delta_after = abs(after_num - num_insert)
    delta_before = abs(before_num - num_insert)

    if np.abs(delta_after) < np.abs(delta_before):
        return after_num, pos_num_insert
    return before_num, pos_before
