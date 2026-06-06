#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""isclose — element-wise closeness check for mutable sequences.

.. warning::

    This is NOT the same shape as ``math.isclose``! Where ``math.isclose``
    returns a single ``bool`` for two scalars, ``scitex_math.isclose`` takes
    two iterables and returns a ``list[bool]`` reporting closeness element by
    element.

    The default tolerances also differ: this helper uses
    ``rel_tol=1e-5, abs_tol=1e-8`` (matching ``numpy.isclose`` defaults), so a
    1e-7 absolute difference is reported as close. ``math.isclose`` uses
    ``rel_tol=1e-9`` by default and rejects such diffs.

    Use :func:`numpy.isclose` or :func:`numpy.allclose` for array semantics
    when interoperating with numpy code. This helper is preserved for
    backward compatibility with downstream scitex-gen users.

Ported from scitex-gen ``misc.py`` as part of the scitex-gen full retirement.
"""
from __future__ import annotations

import math


def isclose(mutable_a, mutable_b):
    """Element-wise closeness comparison of two iterables.

    Parameters
    ----------
    mutable_a : iterable of float
        First sequence.
    mutable_b : iterable of float
        Second sequence (zipped position-wise against ``mutable_a``).

    Returns
    -------
    list of bool
        One bool per pair: True if the pair is close, False otherwise.
        Uses ``rel_tol=1e-5, abs_tol=1e-8``.

    Example
    -------
    >>> isclose([1.0, 2.0, 3.0], [1.0, 2.0001, 3.0])
    [True, True, True]
    >>> isclose([1.0, 2.0, 3.0], [1.0, 2.1, 3.0])
    [True, False, True]
    """
    # Default to numpy.isclose's tolerance (rel_tol=1e-5, abs_tol=1e-8) so
    # this helper is forgiving for typical floating-point comparisons.
    # math.isclose's stricter rel_tol=1e-9 default rejects diffs of 1e-7.
    return [
        math.isclose(a, b, rel_tol=1e-5, abs_tol=1e-8)
        for a, b in zip(mutable_a, mutable_b)
    ]
