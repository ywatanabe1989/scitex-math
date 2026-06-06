#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""is_nan — assert-style NaN detector that raises on any NaN value.

.. warning::

    This is NOT a predicate! Despite the ``is_`` prefix, this function does
    NOT return a bool — it returns ``None`` on success and raises
    ``ValueError`` when any NaN is present. It is closer in spirit to
    ``assert no NaNs`` than to ``numpy.isnan``.

    Use :func:`numpy.isnan` / :meth:`pandas.Series.isna` / :func:`math.isnan`
    when you need a boolean predicate. Use this helper as a guardrail in
    pipelines that should fail fast when NaNs sneak in.

Ported from scitex-gen ``misc.py`` as part of the scitex-gen full retirement.
``torch`` support is optional — if torch is not installed the tensor branch
is skipped.
"""
from __future__ import annotations

import math


def is_nan(X):
    """Raise ``ValueError`` if the input contains any NaN.

    Parameters
    ----------
    X : pandas.DataFrame, numpy.ndarray, torch.Tensor, float, or int
        The input data to scan.

    Returns
    -------
    None
        Returns nothing on success.

    Raises
    ------
    ValueError
        If any NaN value is found in ``X``.

    Example
    -------
    >>> import numpy as np
    >>> is_nan(np.array([1.0, 2.0, 3.0]))  # no NaN -> returns None
    >>> is_nan(np.array([1.0, float('nan'), 3.0]))  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ValueError: NaN was found in X
    """
    import numpy as np
    import pandas as pd

    if isinstance(X, pd.DataFrame):
        if X.isna().any().any():
            raise ValueError("NaN was found in X")
        return None

    if isinstance(X, np.ndarray):
        if np.isnan(X).any():
            raise ValueError("NaN was found in X")
        return None

    # Optional torch support
    try:
        import torch as _torch  # noqa: WPS433

        if _torch.is_tensor(X):
            if X.isnan().any():
                raise ValueError("NaN was found in X")
            return None
    except ImportError:
        pass

    if isinstance(X, (float, int)):
        if math.isnan(X):
            raise ValueError("X was NaN")
        return None

    return None
