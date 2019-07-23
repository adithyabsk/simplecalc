"""A command line interface for a calculator app."""

import click

from simplecalc.calculator import (
    CalculatorTypeError,
    CalculatorValueError,
    difference as d,
    product as p,
    quotient as q,
    sum_ as s,
)


def _exception_handler(op, *args):
    """Handle internally raised exceptions and print to console

    Args:
        op (func): The function to perform
        *args: The function's arguments

    Returns:
        The function's computational result

    """
    try:
        return op(*args)
    except (CalculatorTypeError, CalculatorValueError) as e:
        click.echo(e)


@click.group()
def calc():  # pragma: no cover
    """A simple calculator utility."""
    pass


@calc.command()
@click.argument("numbers", nargs=-1)
def sum(numbers):
    """Finds the sum of a list of numbers."""
    click.echo(_exception_handler(s, numbers))


@calc.command()
@click.argument("numbers", nargs=-1)
def difference(numbers):
    """Finds the difference of a list of numbers."""
    click.echo(_exception_handler(d, numbers))


@calc.command()
@click.argument("numbers", nargs=-1)
def product(numbers):
    """Finds the product of a list of numbers."""
    click.echo(_exception_handler(p, numbers))


@calc.command()
@click.argument("numbers", nargs=-1)
def quotient(numbers):
    """Finds the quotient of a list of numbers."""
    click.echo(_exception_handler(q, numbers))


if __name__ == "__main__":
    calc()
