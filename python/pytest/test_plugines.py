"""
python supports different plugins
1)pytest-html
2) pytest-xdist [to run tests in parallel]


this plugins will help us to run testcases in specific order 
we can change the order of testcase execution using pytest--order

to install :: pip install pytest --order
"""
import pytest
@pytest.fixture()
def web_dev():
    print("Start with html")
    yield
    print("2nd start with css")

# @pytest.mark.regression
def test_javascript(web_dev):
    print("Master javascript")

@pytest.mark.skip(reason= "msg")
def test_angular(web_dev):
    print("Master angular")

def test_reactjs(web_dev):
    print("Master React js")