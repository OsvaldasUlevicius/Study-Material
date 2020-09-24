# text fixtures - snippets of code that run before/after the tests just like setup/teardown methods
# text fixtures allows for a ore individual combination between tests and snippets of code that go with them
# Test fixtures scope - function/ class/ module / session
import pytest

#@pytest.fixture(autouse=True) # true means that it runs before each test # another parameter to use in the paranthesis is scope=session/module/function/class # another parameter is params=[1,2] - optional parameters that cat be passed to the test
# if you pass in the optional parameters in te function use reVal = request.param to retrieve them - then the test and the fixture will run once fore each param specified - just like a loop
@pytest.fixture()
def setup1():
    print('\nSetup')
    yield
    print('\nTeardown 1') # termination code after yield

@pytest.fixture()
def setup2(request):
    print('\nSetup 2')

    def teardown_a():
        print('\nTeardown AAA')

    def teardown_b():
        print('\nTeardown BBB')

    request.addfinalizer(teardown_a) # calls this termination code and likewise below
    request.addfinalizer(teardown_b)

def test1(setup1): # you can add the setup function in between the paranthesis for it to run before this test
    print('Executing test1')
    assert True

#@pytest.mark.usefixtures('setup') - runs setup before this test
def test2(setup2):
    print('Executing test2')
    assert True
