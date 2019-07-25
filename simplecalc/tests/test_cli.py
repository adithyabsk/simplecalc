"""Test the command line interace to the simplecalc API."""

import pytest
from click.testing import CliRunner


def test_exception_handling_valid():
    """Test cli exception handling valid input."""
    from simplecalc.cli import _exception_handler

    def f(n1, n2):
        return n1 + n2

    assert 3 == _exception_handler(f, 1, 2)


def test_exception_handling_error():
    """Test cli exception handling invalid input."""
    from simplecalc.cli import _exception_handler

    def f(test):
        raise Exception("Test")

    with pytest.raises(Exception) as e:
        _exception_handler(f, [])

    assert "Test" in str(e)


@pytest.mark.parametrize(
    "err_class", ["CalculatorTypeError", "CalculatorValueError"]
)
def test_exception_handling_captures_calctypeerror(err_class, capfd):
    """Test exception handling captures input.

    Args:
        capfd: pytest stdout/stderr capture data

    """
    from simplecalc.cli import _exception_handler
    import simplecalc.calculator as calc

    Error = getattr(calc, err_class)

    def f(n1, n2):
        raise Error("Test")

    _exception_handler(f, None, None)

    out, err = capfd.readouterr()
    assert "Test" in out


def test_calc_main():
    """Test main cli runner output."""
    from simplecalc.cli import simplecalc

    runner = CliRunner()
    result = runner.invoke(simplecalc)
    assert result.exit_code == 0
    assert "Usage: simplecalc" in result.output


def test_calc_sum_fail():
    """Test sum failure."""
    from simplecalc.cli import sum as s

    runner = CliRunner()
    result = runner.invoke(s)
    assert result.exit_code == 0
    assert "Input list must have at least two items" in result.output

    runner = CliRunner()
    result = runner.invoke(s, ["Test", "Test"])
    assert result.exit_code == 0
    assert "All inputs must be a number" in result.output


def test_calc_sum():
    """Test sum valid inputs."""
    from simplecalc.cli import sum as s

    runner = CliRunner()
    result = runner.invoke(s, ["1", "0.2", "0.3"])
    assert result.exit_code == 0
    assert pytest.approx(float(result.output)) == 1.5


def test_calc_difference_fail():
    """Test difference command fail cases."""
    from simplecalc.cli import difference

    runner = CliRunner()
    result = runner.invoke(difference)
    assert result.exit_code == 0
    assert "Input list must have at least two items" in result.output

    runner = CliRunner()
    result = runner.invoke(difference, ["Test", "Test"])
    assert result.exit_code == 0
    assert "All inputs must be a number" in result.output


def test_calc_difference():
    """Test difference command with valid inputs."""
    from simplecalc.cli import difference

    runner = CliRunner()
    result = runner.invoke(difference, ["1", "0.2", "0.3"])
    assert result.exit_code == 0
    assert pytest.approx(float(result.output)) == 0.5


def test_calc_product_fail():
    """Test product command with invalid inputs."""
    from simplecalc.cli import product

    runner = CliRunner()
    result = runner.invoke(product)
    assert result.exit_code == 0
    assert "Input list must have at least two items" in result.output

    runner = CliRunner()
    result = runner.invoke(product, ["Test", "Test"])
    assert result.exit_code == 0
    assert "All inputs must be a number" in result.output


def test_calc_product():
    """Test product command with valid inputs."""
    from simplecalc.cli import product

    runner = CliRunner()
    result = runner.invoke(product, ["1", "0.2", "0.3"])
    assert result.exit_code == 0
    assert pytest.approx(float(result.output)) == 0.06


def test_calc_quotient_fail():
    """Test quotient command for failure modes."""
    from simplecalc.cli import quotient

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
        "No items after the first cannot be zero when diving." in result.output
    )


def test_calc_quotient():
    """Test quotient command with valid inputs."""
    from simplecalc.cli import quotient

    runner = CliRunner()
    result = runner.invoke(quotient, ["1", "0.2", "0.3"])
    assert result.exit_code == 0
    assert pytest.approx(float(result.output)) == 16.6666666667
