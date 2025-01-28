# 3) scope = session [fixtures will be called once per entire session]

import pytest

@pytest.fixture(scope='session')
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
    