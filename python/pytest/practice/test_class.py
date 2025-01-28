#  scope = class   [fictures will be called once per test class]

import pytest
@pytest.fixture(scope='class')
def web_dev():
    print("Start with html")
    yield
    print("2nd start with css")

def test_javascript(web_dev):
    print("Master javascript")

def test_angular(web_dev):
    print("Master angular")

def test_reactjs(web_dev):
    print("Master React js")

def test_job(web_dev):
    print("Get a job after that.")
    