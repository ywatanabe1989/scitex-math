#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: /tests/scitex_math/test__float_linspace.py
"""Tests for ``scitex_math.float_linspace`` (ported from scitex_gen.misc)."""

import numpy as np

from scitex_math import float_linspace


class TestFloatLinspace:
    """Test float_linspace function."""

    def test_basic_linspace(self):
        result = float_linspace(0, 1, 5)
        expected = np.array([0.0, 0.25, 0.5, 0.75, 1.0])
        np.testing.assert_array_almost_equal(result, expected)

    def test_three_points(self):
        result = float_linspace(1, 2, 3)
        expected = np.array([1.0, 1.5, 2.0])
        np.testing.assert_array_almost_equal(result, expected)

    def test_single_point(self):
        result = float_linspace(5, 10, 1)
        expected = np.array([5])
        assert np.array_equal(result, expected)

    def test_two_points(self):
        result = float_linspace(0, 10, 2)
        expected = np.array([0, 10])
        assert np.array_equal(result, expected)

    def test_negative_range(self):
        result = float_linspace(-1, 1, 5)
        expected = np.array([-1.0, -0.5, 0.0, 0.5, 1.0])
        np.testing.assert_array_almost_equal(result, expected)

    def test_reverse_range(self):
        result = float_linspace(10, 0, 5)
        expected = np.array([10.0, 7.5, 5.0, 2.5, 0.0])
        np.testing.assert_array_almost_equal(result, expected)

    def test_float_num_points(self):
        result = float_linspace(0, 1, 5.8)
        assert len(result) == 5


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.abspath(__file__)])
