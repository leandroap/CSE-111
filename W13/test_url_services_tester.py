from url_services_tester import is_url_valid, validate_status_code, \
    is_valid_url_pattern, validate_csv_file_pattern
import pytest

def test_is_url_valid():
    """Verify that the is_url_valid function works correctly.
    Parameters: none
    Return: nothing
    """

    assert True  == is_url_valid("https://httpbin.org/status/200")
    assert True  == is_url_valid("https://httpbin.org/status/201")
    assert True  == is_url_valid("https://httpbin.org/status/301")
    assert True  == is_url_valid("https://httpbin.org/status/302")
    assert False == is_url_valid("https://httpbin.org/status/400")
    assert False == is_url_valid("https://httpbin.org/status/500")

def test_validate_status_code():
    """Verify that the validate_status_code function works correctly.
    Parameters: none
    Return: nothing
    """

    assert True  == validate_status_code("https://httpbin.org/status/200", 200)
    assert True  == validate_status_code("https://httpbin.org/status/201", 201)
    assert True  == validate_status_code("https://httpbin.org/status/304", 304)
    assert False == validate_status_code("https://httpbin.org/status/302", 302)
    assert False == validate_status_code("https://httpbin.org/status/400", 200)
    assert False == validate_status_code("https://httpbin.org/status/500", 200)

def test_is_valid_url_pattern():
    """Verify that the test_is_valid_url_pattern function works correctly.
    Parameters: none
    Return: nothing
    """

    assert True  == is_valid_url_pattern("https://leandroap.com")
    assert True  == is_valid_url_pattern("https://amaral.app")
    assert True  == is_valid_url_pattern("https://reginaamaral.com")
    assert True  == is_valid_url_pattern("https://httpbin.org/status/201")
    assert True  == is_valid_url_pattern("https://httpbin.org/status/302")
    assert True  == is_valid_url_pattern("http://httpbin.com")
    assert False == is_valid_url_pattern("httpbin.org/status/500")
    assert False == is_valid_url_pattern("httpbin")
    assert False == is_valid_url_pattern("httpbin.com")

def test_validate_csv_file_pattern():
    assert False == validate_csv_file_pattern("invalid_file.csv")
    #Check if the valid file is at the 'rootdir:' path
    assert True == validate_csv_file_pattern("urls_test_file.csv")

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])