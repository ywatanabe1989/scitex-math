# Changelog

All notable changes to `scitex-math` are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/);
versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [0.2.0]

- Port the remaining numeric / normalization surface from `scitex-gen`:
  - `symlog`, `to_rank`, `transpose`, `connect_nums`, `float_linspace`.
  - `to_z`, `to_nanz`, `to_01`, `to_nan01`, `unbias`, `clip_perc` plus the
    cached variants in `_norm_cache`.
  - `find_closest` — closest element in a sorted list (numpy/bisect).
  - `isclose` — element-wise closeness over zipped iterables, returning
    `list[bool]`. Note: distinct from `math.isclose` (see docstring).
  - `is_nan` — assert-style NaN guard that raises `ValueError` on any NaN
    in DataFrame / ndarray / tensor / scalar input (see docstring).
- Adopt the PEP 562 lazy attribute loader: `import scitex_math` stays cheap
  and pulls in neither `torch` nor `scitex_decorators`.
- New runtime deps: `numpy`, `pandas`, `scitex-decorators`. `torch` is an
  optional extra (`scitex-math[torch]`).

## [0.1.0]

- Initial release. Hosts `to_even` and `to_odd`, the integer-parity
  helpers previously exported by `scitex-gen`. Pure-stdlib core, zero
  runtime dependencies.
