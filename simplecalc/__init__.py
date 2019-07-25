"""Simple calculator API."""

from simplecalc.calculator import (
    CalculatorTypeError,
    CalculatorValueError,
    difference,
    product,
    quotient,
    sum_,
)


__all__ = [
    "CalculatorValueError",
    "CalculatorTypeError",
    "sum_",
    "difference",
    "product",
    "quotient",
]


def get_pyproject():
    import os
    import toml

    init_path = os.path.abspath(os.path.dirname(__file__))
    pyproject_path = os.path.join(init_path, "../pyproject.toml")

    with open(pyproject_path, "r") as fopen:
        pyproject = toml.load(fopen)

    return pyproject["tool"]["poetry"]


__version__ = get_pyproject()["version"]
__doc__ = get_pyproject()["description"]
