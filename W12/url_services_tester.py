# File: url_services_tester.py
# Author: Leandro Amaral Pereira

import requests

def main(): 

    #print(is_url_valid("https://leandroap.com"))
    #print(is_url_valid("https://amaral.app"))
    #print(is_url_valid("https://reginaamaral.com"))
    #print(is_url_valid("https://httpbin.org/status/201"))
    #print(is_url_valid("https://httpbin.org/status/302"))
    #print(is_url_valid("https://httpbin.org/status/404"))
    #print(is_url_valid("https://httpbin.org/status/500"))

    print(validate_status_code("https://leandroap.com", 200))
    print(validate_status_code("https://amaral.app", 200))
    print(validate_status_code("https://reginaamaral.com", 200))
    print(validate_status_code("https://httpbin.org/status/201", 201))
    print(validate_status_code("https://httpbin.org/status/304", 304))
    print(validate_status_code("https://httpbin.org/status/404", 404))
    print(validate_status_code("https://httpbin.org/status/500", 500))



def is_url_valid(url):
    """Verify if an URL is valid
    Parameter: 
        url: string with the URL to validate
    Return: Boolean
        True - HTTP Status code isn't between 4XX and 5XX
        False - HTTP Status code is between 4XX and 5XX or there are any connection error
    """

    is_valid = False

    try:
        response = requests.get(url)
        is_valid = response.raise_for_status() == None

    except requests.HTTPError as http_error:
        print(type(http_error).__name__, http_error, sep=": ")

    except requests.ConnectionError as e:
        print(type(e).__name__, e, sep=": ")

    return is_valid

def validate_status_code(url, expected_code):
    """Verify if an URL is valid
    Parameter: 
        url: string with the URL to validate
        expected_code: HTTP status code to validate
    Return: Boolean
        True - HTTP Status code matches the expected_code
        False - HTTP Status code doesn't match the expected_code
    """
    
    is_valid = False

    try:
        response = requests.get(url)
        is_valid = response.status_code == expected_code

    except requests.HTTPError as http_error:
        print(type(http_error).__name__, http_error, sep=": ")

    except requests.ConnectionError as e:
        print(type(e).__name__, e, sep=": ")

    return is_valid

if __name__ == "__main__":
    main()