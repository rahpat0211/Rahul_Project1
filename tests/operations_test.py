"""Testing the calculator operations """

from calculator.operations import Addition, Subtraction, Multiplication, Division


def test_calculator_operations_add():
    """Testing the Addition caluclation"""
    assert Addition.add(1, 1) == 2


def test_calculator_operations_subtract():
    """Testing the Subtraction calculation"""
    assert Subtraction.subtract(1, 1) == 0


def test_calculator_operations_multiply():
    """Testing the Multiplication calculation"""
    assert Multiplication.multiply(1, 1) == 1


def test_calculator_operations_divide():
    """Testing the Division calculation"""
    assert Division.divide(1, 1) == 1


def test_calculator_operations_divide_by_zero():
    """Testing the Division calculation if divided by 0"""
    assert Division.divide(1, 0) is None
