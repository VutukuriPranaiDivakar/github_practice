"""
Pytest::

        Testing Framework
        writing and execiting testcases
        we can generate test reports
        pytest supports different features
            1) Fixtures
            2) Markers
            3) Data Driven [Parameters]
        Easy to understand and easy to integrate with CI/CD
        Easy to dubug test failures
        
        
    All the testcase names should be start with test_anyname.py :: test_intro.py
    Testcase must be defined with test_
    syntax :: def test_intro() and no need to call it will directly executed


    to execute the pytest file use :: pytest file_name
    to view the output :: pytest -s -v file_name
    when we run testcases with pytest it will search for all the testcases starting test_ and executes
    It will not excutes functions by default

    to print the specific testcase :: pytest -s -v file_name.py::test_casename
    to print multiple specific testcases :: pytest -s -v test_intro.py::test_third_case test_intro.py::test_fourth_case

    we can generate test reports with pytest :: html, xml etc ..
    pip install pytest-html
    to execute that :: pytest --html=file.html test_intro.py


    pytest supports test assertion ::
    assert condition :: ex :: assert x + y = 100 ::error : assertion error (msg)
x
    Pytest supports files like ::
    1) Conftest.py
    2) requriments.txt
    3) markers.ini

    Pytest supports additional feratures like
    1) fixtures
    2) markers
    3) parameterize
    4) hooks
    5) plugins

    python supports different plugins
    1)pytest-html
    2) pytest-xdist [to run tests in parallel]  

    *** if we write the code in conftest.py file it will be available in all the file
        if we write the code in other file it will available in that particular file


    [pytest]

markers = 
    regression : These TC's are executing As part of new release Regression Testing. #pytest.mark.regression
    pref : these TC's are for performance Testing  # @pytest.mark.pref  
    sanity : these are sanity testcases            # @pytest.mark.sanity
    slow : these are long running tc's             # @pytest.mark.slow


# to execute those cmds :: pytest -s -v -m test_name.py


@pytest.mark.skip(reason= "msg")
@pytest.mark.skip(release != "msg")


"""