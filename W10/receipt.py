# File: receipt.py
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson10/prove.html

import csv
from datetime import datetime

PRODUCT_NUMBER_INDEX = 0
PRODUCT_NAME_INDEX = 1
RETAIL_PRICE_INDEX = 2
QUANTITY_INDEX = 1

PRODUCTS_FILE = "products.csv"
REQUESTS_FILE = "request.csv"
STORE_NAME = "Inkom Emporium"
SALES_TAX_RATE = 0.06

def main():

    #Print the store name at the top of the receipt.
    print(f"{STORE_NAME}\n")

    # Calls the read_dictionary function and stores the compound dictionary
    products_dict = read_dictionary(PRODUCTS_FILE, PRODUCT_NUMBER_INDEX)

    # Opens the request.csv file for reading.
    # Skips the first line of the request.csv file because the first line contains column headings.
    requests_list = read_compound_list(REQUESTS_FILE)

    ordered_items, subtotal, \
        sales_tax, total = compute_and_print_ordered_itens(requests_list, products_dict)
    
    print(f"\nNumber of Items: {ordered_items}")
    print(f"Subtotal: {round(subtotal, 2)}")
    print(f"Sales Tax: {round(sales_tax, 2)}")
    print(f"Total: {round(total, 2)}")

    print(f"\nThank you for shopping at the {STORE_NAME}.")
    print(get_current_date_time())

def get_discount():
    """Verify if any discount is avaliable

    Parameters: none
    Return: discount rate
    """
    discount_rate = 0

    current_date_and_time = datetime.now()

    weekday = int(f"{current_date_and_time:%w}")
    hour = int(f"{current_date_and_time:%H}")

    # Write code to discount the product prices by 10% 
    # if today is Tuesday or Wednesday.
    if weekday == 2 or weekday == 3:
        discount_rate = 0.10
    
    # Write code to discount the product prices by 10% 
    # if the current time of day is before 11:00 a.m.
    if hour < 11:
        discount_rate = 0.10

    return discount_rate

def compute_and_print_ordered_itens(requests_list, products_dict):
    ordered_items = 0
    subtotal = 0
    discount_rate = get_discount()

    # Uses a loop that reads and processes each row from the request.csv file.
    for request in requests_list:
        product_number = request[PRODUCT_NUMBER_INDEX]
        requested_quantity = int(request[QUANTITY_INDEX])
        ordered_items += requested_quantity
        
        # Use the requested product number to find the corresponding item in the products_dict.
        try:
            product = products_dict[product_number]
            product_name = product[PRODUCT_NAME_INDEX]
            product_price = float(product[RETAIL_PRICE_INDEX])

            if discount_rate > 0:
                discount = product_price * discount_rate
                product_price = round(product_price - discount, 2)

            subtotal += requested_quantity * product_price

            # Print the product name, requested quantity, and product price.
            print(f"{product_name}: {requested_quantity} @ {product_price}")

        except KeyError as key_error:
            print(f"Error: unknown product ID in the request.csv file\n{key_error}")
    
    sales_tax = subtotal * SALES_TAX_RATE
    total = subtotal + sales_tax

    return ordered_items, subtotal, sales_tax, total

def get_current_date_time():
    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    # Use an f-string to print the current
    # day of the week, month, day, the current time and year.
    return f"{current_date_and_time:%a %b %d %X %Y}"

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}
    try:
        # Open the CSV file for reading and store a reference
        # to the opened file in a variable named csv_file.
        with open(filename, "rt") as csv_file:

            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(csv_file)

            # The first row of the CSV file contains column
            # headings and not data, so this statement skips
            # the first row of the CSV file.
            next(reader)

            # Read the rows in the CSV file one row at a time.
            # The reader object returns each row as a list.
            for row_list in reader:

                # If the current row is not blank, add the
                # data from the current to the dictionary.
                if len(row_list) != 0:

                    # From the current row, retrieve the data
                    # from the column that contains the key.
                    key = row_list[key_column_index]

                    # Store the data from the current
                    # row into the dictionary.
                    dictionary[key] = row_list

    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(f"Error: missing file\n{not_found_err}")

    # Return the dictionary.
    return dictionary

def read_compound_list(filename):
    """Read the contents of a CSV file into a compound
    list and return the list. Each element in the
    compound list will be a small list that contains
    the values from one row of the CSV file.

    Parameter filename: the name of the CSV file to read
    Return: a list of lists that contain strings
    """
    # Create an empty list that will
    # store the data from the CSV file.
    compound_list = []
    try:

        # Open the CSV file for reading and store a reference
        # to the opened file in a variable named csv_file.
        with open(filename, "rt") as csv_file:

            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(csv_file)

            # The first row of the CSV file contains column
            # headings and not data, so this statement skips
            # the first row of the CSV file.
            next(reader)

            # Read the rows in the CSV file one row at a time.
            # The reader object returns each row as a list.
            for row_list in reader:

                # If the current row is not blank,
                # append it to the compound_list.
                if len(row_list) != 0:

                    # Append one row from the CSV
                    # file to the compound list.
                    compound_list.append(row_list)

    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(f"Error: missing file\n{not_found_err}")

    # Return the compound list.
    return compound_list

if __name__ == "__main__":
    main()