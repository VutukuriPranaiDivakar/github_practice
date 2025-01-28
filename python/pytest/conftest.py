"""
It is a special file in pytest, it will be called automatically whenever we run a testcase
all the fixtures will be defined in conftest.py
fictures defined n conftest.py will be available throughtout testcases in same folder

*** what ever u write inside a conftest.py will be executed before the test-- first the control goto this file when u execute a testcase    


ex ::
create folder
    conftest.py
        test1.py
        test2.py

"""

import pytest


a = 100
b = 200
@pytest.fixture
def fun_conftest():
    print("This is a conftest file")    
    assert a + b == 300, ("This is correct way for executing the assert")


    
