#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: /tests/scitex_math/test__connect_nums.py
"""Tests for ``scitex_math.connect_nums`` (ported from scitex_gen.misc)."""

from scitex_math import connect_nums


class TestConnectNums:
    def test_two_zeros(self):
        assert connect_nums((0, 0)) == "0-0"

    def test_three_ints(self):
        assert connect_nums((1, 2, 3)) == "1-2-3"

    def test_strings(self):
        assert connect_nums(("a", "b")) == "a-b"

    def test_floats(self):
        assert connect_nums([1.5, 2.5]) == "1.5-2.5"

    def test_empty(self):
        assert connect_nums([]) == ""

    def test_single_value(self):
        assert connect_nums([42]) == "42"


if __name__ == "__main__":
    import os

    import pytest

    pytest.main([os.path.abspath(__file__)])
