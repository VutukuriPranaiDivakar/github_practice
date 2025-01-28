"""
Markers in pytest are tags that will control flow of executions of pytest testcase
we can mark the testcase with decorators @pytest.mark

inbuilt decorators::
@pytest,mark.skip()
@pytest,mark.skip(reason= "")
@pytest,mark.skipif(condition)
@pytest,mark.fail()
@pytest,mark.xfail()
@pytest,mark.parametrize()

We can create custom markers in pytest

create a file pytest.ini [configuration file] in testcase folder

[pytest]

markers = 
    regression : These TC's are executing As part of new release Regression Testing. #pytest.mark.regression
    pref : these TC's are for performance Testing  # @pytest.mark.pref  
    sanity : these are sanity testcases            # @pytest.mark.sanity
    slow : these are long running tc's             # @pytest.mark.slow

    to run specific markers
    pytest -m <marker_name> <script_name> to  run markers in specific testscript
    pytest -m <marker_name> to run all markers in folders

    # to execute those cmds :: pytest -s -v -m test_name.py

"""
import pytest

@pytest.mark.skip
def test_first():
    print("this is first testcase")

@pytest.mark.xfail
def test_second():
    print("this is second testcase")
@pytest.mark.skipif()
def test_third():
    print("this is third testcase")

@pytest.mark.regression  # to execute this use pytest -s -v -m regression test_filename.py # only that particular testcase will be execute
def test_fourth():
    print("this is foruth testcase")
