# setup functions/ modules/ methods / classes - snippets of code that run before the tests
# termination functions/ methods / classes - snippets of code that run after the tests

def setup_function(function):
    if function == test1:
        print('\nSetting up test1!')
    elif function == test2:
        print("\nSetting up test2!")
    else:
        print("\nSetting up unknown test!")

def teardown_function(function):
    if function == test1:
        print('\nTearing down test1!')
    elif function == test2:
        print("\nTearing down test2!")
    else:
        print("\nTearing down unknown test!")

def test1():
    print("\nExecuting test1")
    assert True


def test2():
    print("\nExecuting test2")
    assert True

