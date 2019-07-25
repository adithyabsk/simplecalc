"""Unit tests for the core calculator."""

import pytest


def test_custom_exceptions():
    """Test that custom exceptions work and are raised."""
    from simplecalc.calculator import CalculatorValueError, CalculatorTypeError

    with pytest.raises(CalculatorValueError) as e1:
        raise CalculatorValueError("Test error")

    assert "Test error" in str(e1)

    with pytest.raises(CalculatorTypeError) as e2:
        raise CalculatorTypeError("Test error")

    assert "Test error" in str(e2)


def test_convet_num():
    """Test that input conversions work."""
    from simplecalc.calculator import _convert_num

    _convert_num("1") == 1
    _convert_num("0.") == 0.0

    with pytest.raises(ValueError):
        _convert_num("None")


def test_check_input_not_list():
    """Test that inputs are of type list."""
    from simplecalc.calculator import _check_input
    from simplecalc.calculator import CalculatorTypeError

    with pytest.raises(CalculatorTypeError) as e:
        _check_input("Test")

    assert "Input must be a list, received: " in str(e)


def test_check_input_list_length():
    """Test that the input length has at least two items."""
    from simplecalc.calculator import _check_input
    from simplecalc.calculator import CalculatorValueError

    with pytest.raises(CalculatorValueError) as e1:
        _check_input([])

    with pytest.raises(CalculatorValueError) as e2:
        _check_input([0])

    with pytest.raises(CalculatorValueError) as e3:
        _check_input(tuple())

    with pytest.raises(CalculatorValueError) as e4:
        _check_input((0,))

    assert "Input list must have at least two items" in str(e1)
    assert "Input list must have at least two items" in str(e2)
    assert "Input list must have at least two items" in str(e3)
    assert "Input list must have at least two items" in str(e4)


def test_check_input_all_numbers_conversion():
    """Test that the input number conversion works on lists."""
    from simplecalc.calculator import _check_input

    l1 = [0, 1, 2]
    l2 = ["0.", "-1.", "3.5"]
    l3 = ["0", "-1", "-10"]

    assert _check_input(l1) == [0, 1, 2]
    assert _check_input(l2) == [0.0, -1.0, 3.5]
    assert _check_input(l3) == [0, -1, -10]


def test_check_input_all_numbers_error():
    """Test that the input conversion fails as required."""
    from simplecalc.calculator import _check_input
    from simplecalc.calculator import CalculatorValueError

    l1 = ["Error", "Erroring", "Erroringest"]
    l2 = ["0", "0.", "test"]

    with pytest.raises(CalculatorValueError) as e1:
        _check_input(l1)

    with pytest.raises(CalculatorValueError) as e2:
        _check_input(l2)

    assert "All inputs must be a number, received: " in str(e1)
    assert "All inputs must be a number, received: " in str(e2)


def test_check_input_protect_division_zero():
    """Test that the input conversion fails when checking for zero."""
    from simplecalc.calculator import _check_input
    from simplecalc.calculator import CalculatorValueError

    valid = [0, 1, 2]
    invalid = ["0", "1", "0."]

    with pytest.raises(CalculatorValueError) as e:
        _check_input(invalid, check_zero=True)

    assert _check_input(valid, check_zero=True) == [0, 1, 2]
    assert "No items after the first cannot be zero when diving." in str(e)


def test_sum():
    """Test the basic sum function."""
    from simplecalc.calculator import sum_

    assert sum_([0, 1]) == 1
    assert sum_([0, 1, -0.1]) == 0.9


def test_difference():
    """Test the basic difference function."""
    from simplecalc.calculator import difference

    assert difference([0, 1, -10, 12]) == -3
    assert difference([0, 1, -0.1]) == -0.9


def test_product():
    """Test the basic product function."""
    from simplecalc.calculator import product

    assert product([0, 1, -10, 12]) == 0
    assert product([1, 3, -0.1]) == pytest.approx(-0.3)


def test_quotient():
    """Test the quotient function along with zero inputs."""
    from simplecalc.calculator import quotient
    from simplecalc.calculator import CalculatorValueError

    with pytest.raises(CalculatorValueError) as e:
        quotient([0, 1, 0])

    assert quotient([0, 1]) == 0
    assert quotient([1, 3, 3]) == pytest.approx(1 / 9)
    assert "No items after the first cannot be zero when diving." in str(e)
