#!/usr/bin/env python3
"""scitex-math — mathematical utilities for the SciTeX ecosystem.

Currently exposes integer-parity helpers extracted from ``scitex_gen``:

- :func:`to_even` — round down to the nearest even integer.
- :func:`to_odd`  — round down to the nearest odd integer.

Future arithmetic helpers (rounding, integer parity, simple numeric
predicates) will live here as well, keeping ``scitex_gen`` focused on
general-purpose utilities and ``scitex_dsp`` / ``scitex_nn`` focused on
signal-processing and neural-network helpers respectively.

Pure-stdlib core — zero runtime dependencies.
"""

from __future__ import annotations

try:
    from importlib.metadata import PackageNotFoundError
    from importlib.metadata import version as _v

    try:
        __version__ = _v("scitex-math")
    except PackageNotFoundError:
        __version__ = "0.0.0+local"
    del _v, PackageNotFoundError
except ImportError:  # pragma: no cover — only on ancient Pythons
    __version__ = "0.0.0+local"

from ._to_even import to_even
from ._to_odd import to_odd

__all__ = [
    "__version__",
    "to_even",
    "to_odd",
]
