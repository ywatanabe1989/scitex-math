#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time-stamp: "2024-11-02 12:50:29 (ywatanabe)"
# File: ./src/scitex_math/_float_linspace.py
"""Evenly spaced floating-point linspace.

Ported from scitex_gen.misc.float_linspace (Phase B retirement wave).
"""

from __future__ import annotations

import numpy as np


def float_linspace(start, stop, num_points):
    """Generate evenly spaced floating-point numbers over a specified interval.

    This function is similar to numpy's linspace, but ensures that the output
    consists of floating-point numbers with a specified number of decimal places.

    Parameters
    ----------
    start : float
        The starting value of the sequence.
    stop : float
        The end value of the sequence.
    num_points : int
        Number of points to generate.

    Returns
    -------
    numpy.ndarray
        Array of evenly spaced floating-point values.

    Example
    -------
    >>> float_linspace(0, 1, 5)
    array([0.  , 0.25, 0.5 , 0.75, 1.  ])
    >>> float_linspace(1, 2, 3)
    array([1. , 1.5, 2. ])
    """
    num_points = int(num_points)  # Ensure num_points is an integer

    if num_points < 2:
        return np.array([start, stop]) if num_points == 2 else np.array([start])

    step = (stop - start) / (num_points - 1)
    values = [start + i * step for i in range(num_points)]

    return np.array(values)


# EOF
