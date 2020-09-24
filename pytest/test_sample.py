def fizzBuzz(value):
    if isMultiple(value, 3) and isMultiple(value, 5):
        return 'FizzBuzz'
    elif isMultiple(value, 3):
        return 'Fizz'
    elif isMultiple(value, 5):
        return 'Buzz'
    return str(value)

def isMultiple(value, mod):
    return value % mod == 0

def checkFizzBuzz(value, expectedReturnValue):
    retVal = fizzBuzz(value)
    assert retVal == expectedReturnValue



def test_returns1():
    checkFizzBuzz(1, "1")

def test_returnsFizzWhen6():
    checkFizzBuzz(6, "Fizz")

def test_returnsBuzzWhen10():
    checkFizzBuzz(10, "Buzz")

def test_returnsFizzBuzzWhen15():
    checkFizzBuzz(15, "FizzBuzzz")
