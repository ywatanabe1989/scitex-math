#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for scitex_math.isclose.

This isclose is *not* math.isclose — it returns ``list[bool]`` over zipped
iterables, with the more permissive numpy.isclose-style tolerances.
"""
from __future__ import annotations

from scitex_math import isclose


class TestIsClose:
    def test_returns_list_of_bools(self):
        result = isclose([1.0, 2.0, 3.0], [1.0, 2.0, 3.0])
        assert isinstance(result, list)
        assert result == [True, True, True]

    def test_tiny_diff_within_tol(self):
        # 1e-7 is bigger than math.isclose default rel_tol=1e-9 but
        # within the numpy-style 1e-5/1e-8 used here.
        result = isclose([2.0], [2.0 + 1e-7])
        assert result == [True]

    def test_large_diff_rejected(self):
        result = isclose([1.0, 2.0, 3.0], [1.0, 2.1, 3.0])
        assert result == [True, False, True]

    def test_zip_truncates_to_shorter(self):
        result = isclose([1.0, 2.0, 3.0], [1.0, 2.0])
        assert result == [True, True]
