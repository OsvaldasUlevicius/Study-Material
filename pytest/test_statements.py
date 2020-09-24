# floating point values are difficult to assert/compare thats why there is approx(0.3) function
# 'raises' statement - when we need to verify that a function throws an exception + 'with' keyword
from pytest import raises

def raisesValueException():
    raise ValueError

def test_exception():
    with raises(ValueError):
        raisesValueException()
