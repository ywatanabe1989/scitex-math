#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for scitex_math.is_nan.

This is_nan is *not* a predicate — it raises ValueError when any NaN
is found, and returns None otherwise.
"""
from __future__ import annotations

import math

import numpy as np
import pandas as pd
import pytest

from scitex_math import is_nan


class TestIsNan:
    def test_ndarray_no_nan_returns_none(self):
        assert is_nan(np.array([1.0, 2.0, 3.0])) is None

    def test_ndarray_with_nan_raises(self):
        with pytest.raises(ValueError, match="NaN was found in X"):
            is_nan(np.array([1.0, float("nan"), 3.0]))

    def test_dataframe_no_nan_returns_none(self):
        assert is_nan(pd.DataFrame({"a": [1, 2, 3]})) is None

    def test_dataframe_with_nan_raises(self):
        with pytest.raises(ValueError, match="NaN was found in X"):
            is_nan(pd.DataFrame({"a": [1.0, float("nan"), 3.0]}))

    def test_scalar_nan_raises(self):
        with pytest.raises(ValueError, match="X was NaN"):
            is_nan(float("nan"))

    def test_scalar_int_returns_none(self):
        assert is_nan(5) is None

    def test_scalar_float_returns_none(self):
        assert is_nan(1.5) is None
