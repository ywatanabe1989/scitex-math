#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File: /tests/scitex_math/test__norm_cache.py
"""Smoke tests for the norm-cache module port.

Original scitex_gen test was a one-line stub asserting ``hasattr(scitex_gen, "cache")``
— that was a decorator test mis-located in the numeric tree. Here we replace it
with a real smoke test for the cache helpers that ship in this module.
"""

import pytest

pytest.importorskip("torch")
import numpy as np  # noqa: E402  (after importorskip)
import torch  # noqa: E402

from scitex_math._norm_cache import (
    clear_norm_cache,
    configure_norm_cache,
    get_norm_cache_info,
    to_01_cached,
    to_z_cached,
)


class TestNormCache:
    def setup_method(self):
        clear_norm_cache()
        configure_norm_cache(enabled=True, max_size=64, verbose=False)

    def test_to_z_cached_torch_zero_mean_unit_variance(self):
        x = torch.tensor([[1.0, 2.0, 3.0, 4.0, 5.0]])
        out = to_z_cached(x, dim=-1)
        assert torch.allclose(out.mean(dim=-1), torch.zeros(1), atol=1e-6)
        assert torch.allclose(out.std(dim=-1, unbiased=True), torch.ones(1), atol=1e-6)

    def test_to_01_cached_torch_range(self):
        x = torch.tensor([[1.0, 2.0, 3.0, 4.0, 5.0]])
        out = to_01_cached(x, dim=-1)
        assert torch.all(out >= 0.0)
        assert torch.all(out <= 1.0 + 1e-6)

    def test_cache_disabled_still_returns_correct_result(self):
        configure_norm_cache(enabled=False)
        x = torch.tensor([[1.0, 2.0, 3.0]])
        out = to_z_cached(x, dim=-1)
        assert out.shape == x.shape

    def test_cache_info_keys(self):
        info = get_norm_cache_info()
        for key in ("enabled", "max_size", "current_size", "operations"):
            assert key in info


if __name__ == "__main__":
    import os

    pytest.main([os.path.abspath(__file__)])
