"""Unit tests for the core calculator."""

import pytest

def test_custom_exceptions():
    from simple_calculator.calculator import (
        CalculatorValueError,
        CalculatorTypeError
    )

    with pytest.raises(CalculatorValueError) as e1:
        raise CalculatorValueError('Test error')

    assert "Test error" in str(e1)

    with pytest.raises(CalculatorTypeError) as e2:
        raise CalculatorTypeError('Test error')

    assert "Test error" in str(e2)

def test_convet_num():
    from simple_calculator.calculator import _convert_num

    _convert_num('1') == 1
    _convert_num('0.') == 0.

    with pytest.raises(ValueError):
        _convert_num('None') == 0.


def test_check_input_not_list():
    from simple_calculator.calculator import _check_input
    from simple_calculator.calculator import CalculatorTypeError

    with pytest.raises(CalculatorTypeError) as e:
        _check_input("Test")

    assert "Input must be a list, received: " in str(e)


def test_check_input_list_length():
    from simple_calculator.calculator import _check_input
    from simple_calculator.calculator import CalculatorValueError

    with pytest.raises(CalculatorValueError) as e1:
        _check_input([])

    with pytest.raises(CalculatorValueError) as e2:
        _check_input([0,])

    with pytest.raises(CalculatorValueError) as e3:
        _check_input(tuple())

    with pytest.raises(CalculatorValueError) as e4:
        _check_input((0,))

    assert "Input list must have at least two items" in str(e1)
    assert "Input list must have at least two items" in str(e2)
    assert "Input list must have at least two items" in str(e3)
    assert "Input list must have at least two items" in str(e4)


def test_check_input_all_numbers_conversion():
    from simple_calculator.calculator import _check_input

    l1 = [0, 1, 2]
    l2 = ["0.", "-1.", "3.5"]
    l3 = ["0", "-1", "-10"]

    assert _check_input(l1) == [0, 1, 2]
    assert _check_input(l2) == [0., -1., 3.5]
    assert _check_input(l3) == [0, -1, -10]


def test_check_input_all_numbers_error():
    from simple_calculator.calculator import _check_input
    from simple_calculator.calculator import CalculatorValueError

    l1 = ["Error", "Erroring", "Erroringest"]
    l2 = ["0", "0.", "test"]

    with pytest.raises(CalculatorValueError) as e1:
        _check_input(l1)

    with pytest.raises(CalculatorValueError) as e2:
        _check_input(l2)

    assert "All inputs must be a number, received: " in str(e1)
    assert "All inputs must be a number, received: " in str(e1)


def test_check_input_protect_division_zero():
    from simple_calculator.calculator import _check_input
    from simple_calculator.calculator import CalculatorValueError

    valid = [0, 1, 2]
    invalid = ["0", "1", "0."]

    with pytest.raises(CalculatorValueError) as e:
        _check_input(invalid, check_zero=True)

    assert _check_input(valid, check_zero=True) == [0, 1, 2]
    assert "No items after the first cannot be zero when diving." in str(e)


def test_check_input_valid():
    from simple_calculator.calculator import _check_input

    assert _check_input([0, 1, 2]) == [0, 1, 2]


def test_sum():
    from simple_calculator.calculator import sum_

    assert sum_([0, 1]) == 1
    assert sum_([0, 1, -0.1]) == 0.9


def test_difference():
    from simple_calculator.calculator import difference

    assert difference([0, 1, -10, 12]) == -3
    assert difference([0, 1, -0.1]) == -0.9


def test_product():
    from simple_calculator.calculator import product

    assert product([0, 1, -10, 12]) == 0
    assert product([1, 3, -0.1]) == pytest.approx(-0.3)


def test_quotient():
    from simple_calculator.calculator import quotient
    from simple_calculator.calculator import CalculatorValueError

    with pytest.raises(CalculatorValueError) as e:
        quotient([0, 1, 0])

    assert quotient([0, 1]) == 0
    assert quotient([1, 3, 3]) == pytest.approx(1/9)
    assert "No items after the first cannot be zero when diving." in str(e)
