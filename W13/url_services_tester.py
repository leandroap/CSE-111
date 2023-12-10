# File: url_services_tester.py
# Author: Leandro Amaral Pereira

import requests
import re
import getopt, sys
import csv

URL_INDEX = 0
HTTP_CODE_INDEX = 1

def command_line_runner(argumentList):
    """Execute the program in the command line mode
    Parameters: none
    Return: nothing
    """

    # Options
    options = "hu:c:f:i"

    # Long options
    long_options = ["help", "url=", "code=", "file=", "input"]

    url_arg  = None
    http_code_arg = None
    filename_arg = None

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)
        
        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):
                print_help()
            
            elif currentArgument in ("-u", "--url"):
                url_arg = currentValue
            
            elif currentArgument in ("-c", "--code"):
                try:
                    http_code_arg = int(currentValue)
                except ValueError as value_error:
                    http_code_arg = -1
                    print(f"\nInvalid value for {currentArgument} argument")
                    print_command_line_usage()
                
            elif currentArgument in ("-f", "--file"):
                if validate_csv_file_pattern(currentValue):
                    filename_arg = currentValue
                else:
                    print(f"\nInvalid csv file for {currentArgument} argument")
                    print_command_line_usage()
            elif currentArgument in ("-i", "--input"):
                main()

        if url_arg != None and http_code_arg != None and http_code_arg != -1:
            print(f"URL to validate: {url_arg}")
            print(f"Expected code: {http_code_arg}")
            print(f"Valid: {validate_status_code(url_arg, http_code_arg)}")

        elif url_arg != None and http_code_arg != -1:
            print(f"URL to validate: {url_arg}")
            print(f"Valid: {is_url_valid(url_arg)}")

        elif filename_arg != None:
            validate_urls_from_file(filename_arg)
                
    except getopt.error as err:
        # output error, and return with an error code
        print (f"\nError: {str(err)}")

        print_command_line_usage()

def print_help():
    """Print instructions for using the program from the command line.
    Parameters: none
    Return: nothing
    """

    usage_example = "Example usage:\n" + \
        "\tpython url_services_tester.py --help\n" + \
        "\tpython url_services_tester.py --input\n" + \
        "\tpython url_services_tester.py --url https://leandroap.com\n" + \
        "\tpython url_services_tester.py --url https://leandroap.com --code 200\n" + \
        "\tpython url_services_tester.py --file /Users/leandro/urls.csv\n"

    print_command_line_usage()
    print(usage_example)

def print_command_line_usage():
    """Print instructions for using the program from the command line.
    Parameters: none
    Return: nothing
    """

    usage_text = "\nUsage: python url_services_tester.py [-h | --help] " + \
        "[-u <url> | --url <url>]\n\t\t\t\t     " + \
        "[-c <http code> | --code <http code>]\n\t\t\t\t     " + \
        "[-f <filename> | --file <filename>]\n\t\t\t\t     " + \
        "[-i | --input]"

    print(usage_text)

def main(): 
    print_elements("header")

    keep_running = True

    while keep_running:
        action = show_menu()

        if action == 1:
            url_entry()
        elif action == 2:
            url_code_entry()
        elif action == 3:
            csv_file_entry()
        elif action == 4:
            print_help()
        elif action == 5:
            keep_running = quit()

def url_entry():
    """Ask the user to enter a URL for validation.
    Parameters: none
    Return: nothing
    """

    url = input("\nPlease enter a URL you want to validate (e.g., https://amaral.app): ")
    
    if is_valid_url_pattern(url):
        print(f"URL to validate: {url}")
        print(f"Valid: {is_url_valid(url)}\n")
    else:
        print(f"\nThe URL {url} appears to be invalid.\nPlease enter a valid URL, such as https://www.example.com\n")

def url_code_entry():
    """Ask the user to enter a URL and HTTP status code for validation.
    Parameters: none
    Return: nothing
    """
    url = input("\nPlease enter a URL you want to validate (e.g., https://leandroap.com): ")
    expected_code = input("Type the expected http status code (Ex.: 200): ")
    
    try:
        if is_valid_url_pattern(url):
            print(f"URL to validate: {url}")
            expected_code = int(expected_code)
            print(f"Expected code: {expected_code}")
            print(f"Valid: {is_url_valid(url)}\n")
        else:
            print(f"\nThe URL {url} appears to be invalid.\nPlease enter a valid URL, such as https://www.example.com\n")
    except ValueError:
        print(f"\nThe code '{expected_code}' appears to be invalid.\n")

# Function of Action 4. CSV filename entry
def csv_file_entry():
    """Ask the user to enter a CSV filename with path for validation.
    Parameters: none
    Return: nothing
    """
    filename = input("\nPlease enter a csv filename with path you want \nto validate (e.g., /Users/leandro/urls.csv): ")

    if validate_csv_file_pattern(filename):
        validate_urls_from_file(filename)
    else:
        print(f"\nThe file '{filename}' appears to be invalid.\n")

# Function of Action 5. Quit
def quit():
    print_elements("footer")

    return False

def is_url_valid(url):
    """Check if a URL is valid.
    Parameter: 
        url: string with the URL to validate
    Return: Boolean
        True - HTTP Status code isn't between 4XX and 5XX
        False - HTTP Status code is between 4XX and 5XX or there are any connection error
    """

    is_valid = False

    if is_valid_url_pattern(url):
        try:
            response = requests.get(url)
            is_valid = response.raise_for_status() == None

        except requests.HTTPError as http_error:
            print(type(http_error).__name__, http_error, sep=": ")

        except requests.ConnectionError as e:
            print(type(e).__name__, e, sep=": ")

    return is_valid

def validate_status_code(url, expected_code):
    """Check if a URL is valid and returned the expected HTTP status code.
    Parameter: 
        url: string with the URL to validate
        expected_code: HTTP status code to validate
    Return: Boolean
        True - HTTP Status code matches the expected_code
        False - HTTP Status code doesn't match the expected_code
    """
    
    is_valid = False

    if is_valid_url_pattern(url):
        try:
            response = requests.get(url)
            is_valid = response.status_code == expected_code

        except requests.HTTPError as http_error:
            print(type(http_error).__name__, http_error, sep=": ")

        except requests.ConnectionError as e:
            print(type(e).__name__, e, sep=": ")

    return is_valid

def is_valid_url_pattern(url):
    """Check if a URL has the valid pattern
    Parameter: 
        url: string with the URL to validate
    Return: Boolean
        True - URL matches the pattern
        False - URL doesn't match the pattern
    """  

    pattern = re.compile(
        r'^(?:http|ftp)s?://'  # Scheme
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # Domain
        r'localhost|'  # Localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # IP address
        r'(?::\d+)?'  # Port (optional)
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)  # Path and query (optional)
    
    return bool(pattern.match(url))

def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []
    
    try:

        # Open the CSV file for reading.
        with open(filename, "rt") as csv_file:

            # Use the csv module to create a reader
            # object that will read from the opened file.
            reader = csv.reader(csv_file)

            # Process each row in the CSV file.
            for row in reader:

                # Append the current row at the end of the compound list.
                compound_list.append(row)
    
    except FileNotFoundError as not_found_err:
        print(type(not_found_err).__name__, not_found_err, sep=": ")

    return compound_list

def validate_urls_from_file(filename):
    """Read entries from a file where each line may include a URL 
        and/or an HTTP status code for verification.
    Parameter: 
        filename with the path for a csv file
    Return: Boolean
        True - HTTP Status code matches the expected_code
        False - HTTP Status code doesn't match the expected_code
    """
    urls_compound_list = read_compound_list(filename)

    for item_list in urls_compound_list:
        url = None
        http_code = None

        if not is_valid_url_pattern(item_list[URL_INDEX]):
            continue

        if len(item_list) > 1:
            url = item_list[URL_INDEX]

            try:
                http_code = int(item_list[HTTP_CODE_INDEX])
            except ValueError as value_error:
                continue
            
            print(f"URL to validate: {url}")
            print(f"Expected code: {http_code}")
            print(f"Valid: {validate_status_code(url, http_code)}")

        else:
            url = item_list[URL_INDEX]
            print(f"URL to validate: {url}")
            print(f"Valid: {is_url_valid(url)}")

def validate_csv_file_pattern(filename):
    """Check if the filename is a valid csv file
    Parameter: 
        url: string with the csv filename
    Return: Boolean
        True - Is a valid csv file
        False - Isn't a valid csv file
    """  
    is_valid_file = True

    try:
        with open(filename, "rt") as csv_file:
            dialect = csv.Sniffer().sniff(csv_file.read(1024))

    except (FileNotFoundError, TypeError, csv.Error) as file_error:
        is_valid_file = False
        print(type(file_error).__name__, file_error, sep=": ")
    
    return is_valid_file

def show_menu():
    action = 0
    
    print(
        "Please select one of the following: \n" \
        "1. Validate single URL\n" \
        "2. Validate URL and HTTP status code\n" \
        "3. Validate from CSV file\n" \
        "4. Show command line Help\n" \
        "5. Quit\n" \
    )

    # To prevent invalid entries
    while action not in range(1, 6):
        # To prevent non numeric entries
        try:
            action = int(input("Please enter an action: ") or 0)
        except:
            action = 0

    return action

# Function to print some decorative elements
def print_elements(option): 
    break_line = "\n****************************************************\n"
    header       = "*      Welcome to the URL and Services Tester      *"
    footer       = "*                  Thank you! Bye.                 *"

    if option == "header":
        print(f"{break_line}{header}{break_line}")
    elif option == "footer":
        print(f"{break_line}{footer}{break_line}")

if __name__ == "__main__":

    argumentList = sys.argv[1:]

    if len(argumentList) > 0:
        command_line_runner(argumentList)
    else:
        main()