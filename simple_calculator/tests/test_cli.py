import pytest
import click
from click.testing import CliRunner

def test_exception_handling_valid():
    from simple_calculator.cli import _exception_handler

    def f(n1, n2):
        return n1 + n2

    assert 3 == _exception_handler(f, 1, 2)


def test_exception_handling_error():
    from simple_calculator.cli import _exception_handler
    from simple_calculator.calculator import (
        CalculatorTypeError,
        CalculatorValueError
    )

    def f(test):
        raise Exception('Test')

    with pytest.raises(Exception) as e:
        _exception_handler(f, [])

    assert 'Test' in str(e)


def test_exception_handling_captures_calctypeerror(capfd):
    from simple_calculator.cli import _exception_handler
    from simple_calculator.calculator import CalculatorTypeError

    def f(n1, n2):
        raise CalculatorTypeError('Test')

    _exception_handler(f, None, None)

    out, err = capfd.readouterr()
    assert "Test" in out


def test_exception_handling_captures_calcvalueerror(capfd):
    from simple_calculator.cli import _exception_handler
    from simple_calculator.calculator import CalculatorValueError

    def f(n1, n2):
        raise CalculatorValueError('Test')

    _exception_handler(f, None, None)

    out, err = capfd.readouterr()
    assert "Test" in out


def test_calc_main():
    from simple_calculator.cli import calc

    runner = CliRunner()
    result = runner.invoke(calc)
    assert result.exit_code == 0
    assert "Usage: calc" in result.output


def test_calc_sum_fail():
    from simple_calculator.cli import sum as s

    runner = CliRunner()
    result = runner.invoke(s)
    assert result.exit_code == 0
    assert "Input list must have at least two items" in result.output

    runner = CliRunner()
    result = runner.invoke(s, ["Test", "Test"])
    assert result.exit_code == 0
    assert "All inputs must be a number" in result.output


def test_calc_sum():
    from simple_calculator.cli import sum as s
    runner = CliRunner()
    result = runner.invoke(s, ["1", "0.2", "0.3"])
    assert result.exit_code == 0
    assert pytest.approx(float(result.output)) == 1.5


def test_calc_difference_fail():
    from simple_calculator.cli import difference

    runner = CliRunner()
    result = runner.invoke(difference)
    assert result.exit_code == 0
    assert "Input list must have at least two items" in result.output

    runner = CliRunner()
    result = runner.invoke(difference, ["Test", "Test"])
    assert result.exit_code == 0
    assert "All inputs must be a number" in result.output


def test_calc_difference():
    from simple_calculator.cli import difference
    runner = CliRunner()
    result = runner.invoke(difference, ["1", "0.2", "0.3"])
    assert result.exit_code == 0
    assert pytest.approx(float(result.output)) == 0.5


def test_calc_product_fail():
    from simple_calculator.cli import product

    runner = CliRunner()
    result = runner.invoke(product)
    assert result.exit_code == 0
    assert "Input list must have at least two items" in result.output

    runner = CliRunner()
    result = runner.invoke(product, ["Test", "Test"])
    assert result.exit_code == 0
    assert "All inputs must be a number" in result.output


def test_calc_product():
    from simple_calculator.cli import product
    runner = CliRunner()
    result = runner.invoke(product, ["1", "0.2", "0.3"])
    assert result.exit_code == 0
    assert pytest.approx(float(result.output)) == 0.06


def test_calc_quotient_fail():
    from simple_calculator.cli import quotient

    runner = CliRunner()
    result = runner.invoke(quotient)
    assert result.exit_code == 0
    assert "Input list must have at least two items" in result.output

    runner = CliRunner()
    result = runner.invoke(quotient, ["Test", "Test"])
    assert result.exit_code == 0
    assert "All inputs must be a number" in result.output

    runner = CliRunner()
    result = runner.invoke(quotient, ["0", "1", "0"])
    assert result.exit_code == 0
    assert (
        "No items after the first cannot be zero when diving." 
        in result.output
    )


def test_calc_quotient():
    from simple_calculator.cli import quotient
    runner = CliRunner()
    result = runner.invoke(quotient, ["1", "0.2", "0.3"])
    assert result.exit_code == 0
    assert pytest.approx(float(result.output)) == 16.6666666667