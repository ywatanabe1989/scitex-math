# scitex-math

<p align="center">
  <a href="https://scitex.ai">
    <img src="docs/scitex-logo-blue-cropped.png" alt="SciTeX" width="400">
  </a>
</p>

<p align="center"><b>Mathematical utilities for the SciTeX ecosystem — parity helpers and friends.</b></p>

<p align="center">
  <a href="https://scitex-math.readthedocs.io/">Full Documentation</a> · <code>uv pip install scitex-math</code>
</p>

<!-- scitex-badges:start -->
<p align="center">
  <a href="https://pypi.org/project/scitex-math/"><img src="https://img.shields.io/pypi/v/scitex-math.svg" alt="PyPI"></a>
  <a href="https://pypi.org/project/scitex-math/"><img src="https://img.shields.io/pypi/pyversions/scitex-math.svg" alt="Python"></a>
  <a href="https://github.com/ywatanabe1989/scitex-math/actions/workflows/pytest-matrix-on-ubuntu-py3-11-3-12-3-13.yml"><img src="https://github.com/ywatanabe1989/scitex-math/actions/workflows/pytest-matrix-on-ubuntu-py3-11-3-12-3-13.yml/badge.svg" alt="Tests"></a>
  <a href="https://www.gnu.org/licenses/agpl-3.0"><img src="https://img.shields.io/badge/license-AGPL_v3-blue.svg" alt="License: AGPL v3"></a>
</p>
<!-- scitex-badges:end -->

---

## Installation

```bash
pip install scitex-math
```

## Architecture

```
scitex_math/
├── _to_even.py    ← to_even — round down to nearest even integer
└── _to_odd.py     ← to_odd  — round down to nearest odd integer
```

Pure-stdlib core — zero runtime deps.

## Quick Start

```python
from scitex_math import to_even, to_odd

to_even(5)    # 4
to_even(6)    # 6
to_even(3.7)  # 2
to_even(-2.3) # -4

to_odd(6)     # 5
to_odd(7)     # 7
to_odd(5.8)   # 5
```

## Status

Standalone module split out of `scitex-gen`. Same semantics as the
original `scitex_gen.to_even` / `scitex_gen.to_odd` — those exports
have been removed from `scitex-gen`; import from `scitex_math` instead.

## Part of SciTeX

`scitex-math` is part of [**SciTeX**](https://scitex.ai).

>Four Freedoms for Research
>
>0. The freedom to **run** your research anywhere — your machine, your terms.
>1. The freedom to **study** how every step works — from raw data to final manuscript.
>2. The freedom to **redistribute** your workflows, not just your papers.
>3. The freedom to **modify** any module and share improvements with the community.
>
>AGPL-3.0 — because we believe research infrastructure deserves the same freedoms as the software it runs on.

## License

AGPL-3.0-only (see [LICENSE](./LICENSE)).

---

<p align="center">
  <a href="https://scitex.ai" target="_blank"><img src="docs/scitex-icon-navy-inverted.png" alt="SciTeX" width="40"/></a>
</p>
