#!/usr/bin/env python3
"""scitex-math — mathematical utilities for the SciTeX ecosystem.

Public API
----------
Integer parity (pure stdlib):
- :func:`to_even` — round down to the nearest even integer.
- :func:`to_odd`  — round down to the nearest odd integer.

Numeric transforms (numpy / torch):
- :func:`symlog`         — symmetric log transformation.
- :func:`to_rank`        — rank transform with tie averaging.
- :func:`transpose`      — array transpose by named dims.
- :func:`connect_nums`   — join values with hyphens.
- :func:`float_linspace` — evenly spaced floats.

Normalization (torch-first, also accepts numpy via @torch_fn):
- :func:`to_z`, :func:`to_nanz`   — z-score / nan-aware z-score.
- :func:`to_01`, :func:`to_nan01` — min-max / nan-aware min-max scaling.
- :func:`unbias`                  — subtract mean/min along a dim.
- :func:`clip_perc`               — clip to percentile bounds.

PEP 562 lazy attribute loading — ``import scitex_math`` is cheap and
pulls in neither torch nor scitex_decorators. Heavy symbols load on
first attribute access.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Version
# ---------------------------------------------------------------------------
try:
    from importlib.metadata import PackageNotFoundError
    from importlib.metadata import version as _v

    try:
        __version__ = _v("scitex-math")
    except PackageNotFoundError:
        __version__ = "0.0.0+local"
    del _v, PackageNotFoundError
except ImportError:  # pragma: no cover - only on ancient Pythons
    __version__ = "0.0.0+local"


# ---------------------------------------------------------------------------
# PEP 562 lazy attribute map: public-name -> relative submodule.
# Each public name equals the attribute name in that submodule.
# ---------------------------------------------------------------------------
_LAZY_ATTRS: dict[str, str] = {
    # Stdlib-only (no torch / numpy import on first access)
    "to_even": "._to_even",
    "to_odd": "._to_odd",
    "connect_nums": "._connect_nums",
    # Numpy-only
    "symlog": "._symlog",
    "float_linspace": "._float_linspace",
    # Torch-backed (lazy: torch only loaded on first access)
    "to_rank": "._to_rank",
    "transpose": "._transpose",
    "to_z": "._norm",
    "to_nanz": "._norm",
    "to_01": "._norm",
    "to_nan01": "._norm",
    "unbias": "._norm",
    "clip_perc": "._norm",
}


def _load_lazy_attr(name: str):
    """Resolve a `_LAZY_ATTRS` name and cache it."""
    from importlib import import_module

    mod_name = _LAZY_ATTRS.get(name)
    if mod_name is None:
        return None
    mod = import_module(mod_name, __name__)
    attr = getattr(mod, name)
    globals()[name] = attr
    return attr


def __getattr__(name: str):
    """PEP 562 lazy-loader: import on first access, cache, return."""
    if _LAZY_ATTRS.get(name) is not None:
        return _load_lazy_attr(name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__() -> list[str]:
    return sorted(set(_LAZY_ATTRS) | set(globals()))


__all__ = [
    "__version__",
    "clip_perc",
    "connect_nums",
    "float_linspace",
    "symlog",
    "to_01",
    "to_even",
    "to_nan01",
    "to_nanz",
    "to_odd",
    "to_rank",
    "to_z",
    "transpose",
    "unbias",
]
