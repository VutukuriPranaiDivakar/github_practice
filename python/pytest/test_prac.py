import pytest

# 1) scope = module  [fixtures will be called once per module] or The fixture is created once for all tests in a module.

@pytest.fixture(scope='module')
def web():
    print("this is html") # 1
    yield
    print("this is css") # 5

def test_js(web):
    print("this is javascript") # 2

def test_react(web):
    print("this is a react") # 3

def test_angular(web):
    print("this is a angular") # 4