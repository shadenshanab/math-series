from math_series.fibonacci import fib
import pytest

#__init__.py in testing
# import pytest
# expected and actual

def test_zero():
    actual = fib(0)
    expected = 0
    assert actual == expected

def test_one():
    actual = fib(1)
    expected = 1
    assert actual == expected

def test_two():
    actual = fib(9)
    expected = 34
    assert actual == expected
