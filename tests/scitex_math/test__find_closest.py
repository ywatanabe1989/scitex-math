#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for scitex_math.find_closest."""
from __future__ import annotations

import math

import numpy as np
import pytest

from scitex_math import find_closest


class TestFindClosest:
    def test_exact_match_lowest(self):
        val, pos = find_closest([1, 3, 5, 7, 9], 1)
        assert val == 1
        assert pos == 0

    def test_basic_in_middle(self):
        val, pos = find_closest([1, 3, 5, 7, 9], 6)
        assert val == 5
        assert pos == 2

    def test_basic_closer_to_after(self):
        val, pos = find_closest([1, 3, 5, 7, 9], 8)
        assert val == 7
        assert pos == 3

    def test_left_edge_below(self):
        val, pos = find_closest([1, 3, 5, 7, 9], 0)
        assert val == 1
        assert pos == 0

    def test_right_edge_above(self):
        val, pos = find_closest([1, 3, 5, 7, 9], 10)
        assert val == 9
        assert pos == 5

    def test_nan_input_returns_nan(self):
        val, pos = find_closest([1, 3, 5, 7, 9], float("nan"))
        assert math.isnan(val)
        assert math.isnan(pos)

    def test_numpy_input(self):
        arr = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
        val, pos = find_closest(arr, 2.4)
        assert val == 2.0
        assert pos == 2
