"""scitex-math quickstart: integer-parity helpers."""

from scitex_math import to_even, to_odd


def main():
    # to_even: round DOWN to the nearest even integer.
    assert to_even(5) == 4
    assert to_even(6) == 6
    assert to_even(3.7) == 2
    assert to_even(-2.3) == -4
    print("to_even ok")

    # to_odd: round DOWN to the nearest odd integer.
    assert to_odd(6) == 5
    assert to_odd(7) == 7
    assert to_odd(5.8) == 5
    print("to_odd ok")


if __name__ == "__main__":
    main()
