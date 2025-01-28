"""
fixtures :: fixtures are functions in python which are decorated with @pytest.fixture
            These are mainly used to setup and cleanup activities for testcases.
            test execution order::
            1) setup the ficture will be executed till yield
            2) Actual Testcase
            3) Cleanup Code

we can define  the scope for fixtures
1) scope = module  [fixtures will be called once per module]
2) scope = function[fixtures will be called once per test function]
3) scope = session [fixtures will be called once per entire session]
4) scope = class   [fictures will be called once per test class]

Default scope of the fixture is function

"""
import pytest
import os
# @pytest.fixture(scope="function")
@pytest.fixture(scope="session")
def setup():
    print("THis is first line") # first execution
    yield
    print("This is second line.") # third execution


def test_setup(setup):
    print("This is a testsetup testcase") # second execution

# def test_second(setup):
#     out = os.popen("dir")
#     print(out.read())