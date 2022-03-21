"""Testing the Calculator"""
import pytest
from calculator.history import Calculations as History
from calculator.calculations import Addition, Subtraction, Multiplication, Division


@pytest.fixture
def clear_history_fixture():
    """define a function that will run each time you pass it to a test, it is called a fixture"""
    # pylint: disable=redefined-outer-name
    History.clear_history()


@pytest.fixture
def setup_addition_calculation_fixture():
    """Addition fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    addition = Addition(values)
    History.add_calculation(addition)


@pytest.fixture
def setup_subtraction_calculation_fixture():
    """Subtraction fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    subtraction = Subtraction(values)
    History.add_calculation(subtraction)


@pytest.fixture
def setup_multiplication_calculation_fixture():
    """Multiplication fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    multiplication = Multiplication(values)
    History.add_calculation(multiplication)


@pytest.fixture
def setup_division_calculation_fixture():
    """Division fixture"""
    # pylint: disable=redefined-outer-name
    values = (1, 2)
    division = Division(values)
    History.add_calculation(division)


def test_add_calculation_to_history(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 1


def test_sub_calculation_to_history(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 1


def test_mul_calculation_to_history(clear_history_fixture,
setup_multiplication_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 1


def test_div_calculation_to_history(clear_history_fixture, setup_division_calculation_fixture):
    """Testing clear history returns true for success"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 1


def test_clear_add_calculation_history(clear_history_fixture, setup_addition_calculation_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 1
    History.clear_history()
    assert History.count_history() == 0
    assert History.clear_history() == True


def test_clear_sub_calculation_history(clear_history_fixture,
setup_subtraction_calculation_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 1
    History.clear_history()
    assert History.count_history() == 0
    assert History.clear_history() == True


def test_clear_mul_calculation_history(clear_history_fixture,
setup_multiplication_calculation_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 1
    History.clear_history()
    assert History.count_history() == 0
    assert History.clear_history() == True


def test_clear_div_calculation_history(clear_history_fixture, setup_division_calculation_fixture):
    """testing clear history"""
    # pylint: disable=unused-argument,redefined-outer-name,singleton-comparison
    assert History.count_history() == 1
    History.clear_history()
    assert History.count_history() == 0
    assert History.clear_history() == True


def test_add_get_calculation(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_calculation(0).get_result() == 3


def test_sub_get_calculation(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing getting a specific calculation out of the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_calculation(0).get_result() == -3


def test_add_get_calc_last_result_value(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_last_calculation_result_value() == 3


def test_sub_get_calc_last_result_value(clear_history_fixture,
setup_subtraction_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_last_calculation_result_value() == -3


def test_add_get_calculation_first(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_first_calculation().get_result() == 3


def test_sub_get_calculation_first(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.get_first_calculation().get_result() == -3


def test_add_history_count(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.count_history() == 1


def test_sub_history_count(clear_history_fixture, setup_subtraction_calculation_fixture):
    """Testing getting the count of calculations from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert History.count_history() == 1


def test_add_get_calc_last_result_object(clear_history_fixture, setup_addition_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # This test if it returns the last calculation as an object
    assert isinstance(History.get_last_calculation_object(), Addition)


def test_sub_get_calc_last_result_object(clear_history_fixture,
setup_subtraction_calculation_fixture):
    """Testing getting the last calculation from the history"""
    # pylint: disable=unused-argument,redefined-outer-name
    # This test if it returns the last calculation as an object
    assert isinstance(History.get_last_calculation_object(), Subtraction)
