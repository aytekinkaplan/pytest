import pytest

import source.my_function as my_functions


def test_add():
    result = my_functions.add(1, 2)
    assert result == 3
    result = my_functions.add(0, 0)
    assert result == 0
    result = my_functions.add(-1, 1)
    assert result == 0
    result = my_functions.add(-1, -1)
    assert result == -2
    result = my_functions.add(1, -1)
    assert result == 0


def test_add_strings():
    result = my_functions.add("I like to eat ", "pizza")
    assert result == "I like to eat pizza"


def test_subtract():
    result = my_functions.subtract(1, 2)
    assert result == -1
    result = my_functions.subtract(0, 0)
    assert result == 0
    result = my_functions.subtract(-1, 1)
    assert result == -2
    result = my_functions.subtract(-1, -1)
    assert result == 0
    result = my_functions.subtract(1, -1)
    assert result == 2


def test_multiply():
    result = my_functions.multiply(1, 2)
    assert result == 2
    result = my_functions.multiply(0, 0)
    assert result == 0
    result = my_functions.multiply(-1, 1)
    assert result == -1
    result = my_functions.multiply(-1, -1)
    assert result == 1
    result = my_functions.multiply(1, -1)
    assert result == -1


def test_divide():
    result = my_functions.divide(1, 2)
    assert result == 0.5
    result = my_functions.divide(0, 1)
    assert result == 0
    result = my_functions.divide(-1, 1)
    assert result == -1
    result = my_functions.divide(-1, -1)
    assert result == 1
    result = my_functions.divide(1, -1)
    assert result == -1


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        my_functions.divide(1, 0)


def test_invalid_input():
    with pytest.raises(TypeError):
        my_functions.add("a", "b")
    with pytest.raises(TypeError):
        my_functions.add(1, "b")
    with pytest.raises(TypeError):
        my_functions.add("a", 1)
