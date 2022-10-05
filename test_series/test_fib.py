from math_series.series import fib, lucas,sum_series
import pytest

#__init__.py in testing
# import pytest
# expected and actual

def test_zero_fib():
    actual = fib(0)
    expected = 0
    assert actual == expected

def test_one_fib():
    actual = fib(1)
    expected = 1
    assert actual == expected

def test_two_fib():
    actual = fib(9)
    expected = 34
    assert actual == expected

def test_zero_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_one_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected

def test_two_lucas():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_one_sum():  # fibonacci
    actual = sum_series(9)
    excepted = 34
    assert actual == excepted


def test_two_sum():  # lucas
    actual = sum_series(7, 2, 1)
    excepted = 29
    assert actual == excepted


def test_three_sum():  # random
    actual = sum_series(9,4,4)
    excepted = 136
    assert actual == excepted

