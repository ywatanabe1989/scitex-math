#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PS-303 — pin the quickstart example by running it as a real
subprocess.

The audit rule (``[PS-303 §3 example-without-test]``) requires every
file under ``examples/`` to have a matching ``tests/examples/test_*.py``.
The test below invokes ``examples/quickstart.py`` as a subprocess
through the live Python interpreter so the file's behavioural assertions
(``to_even`` / ``to_odd`` round-down semantics) are exercised end-to-end
on every CI run — a regression in either helper or in the umbrella's
``__init__`` re-exports turns the example red here first.

We deliberately do NOT import ``examples.quickstart`` and call ``main()``
in-process: the quickstart is the user-facing form, and a successful
process-level invocation is a stronger guarantee than a function call
that bypasses (e.g.) ``if __name__ == '__main__'`` gating.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parents[2]
_QUICKSTART = _REPO_ROOT / "examples" / "quickstart.py"


def test_quickstart_runs_to_completion():
    # Arrange
    cmd = [sys.executable, str(_QUICKSTART)]
    # Act
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    # Assert
    assert result.returncode == 0, (
        f"quickstart.py exited {result.returncode}\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )


def test_quickstart_prints_to_even_ok_marker():
    # Arrange
    cmd = [sys.executable, str(_QUICKSTART)]
    # Act
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    # Assert
    assert "to_even ok" in result.stdout


def test_quickstart_prints_to_odd_ok_marker():
    # Arrange
    cmd = [sys.executable, str(_QUICKSTART)]
    # Act
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    # Assert
    assert "to_odd ok" in result.stdout


# EOF
