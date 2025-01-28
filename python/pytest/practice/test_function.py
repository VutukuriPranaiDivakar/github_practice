# 2) scope = function[fixtures will be called once per test function]

import pytest

# function will be default
@pytest.fixture(scope="function")
def web_dev():
    print("Start with html")
    yield
    print("2nd start with css")

def test_javascript(web_dev):
    print("Master javascript")

def test_angular(web_dev):
    print("Master angular")