# File: receipt.py
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson09/prove.html

import csv

PRODUCT_NUMBER_INDEX = 0
PRODUCT_NAME_INDEX = 1
RETAIL_PRICE_INDEX = 2
QUANTITY_INDEX = 1

def main():
    PRODUCTS_FILE = "products.csv"
    REQUESTS_FILE = "request.csv"

    # Calls the read_dictionary function and stores the compound dictionary
    products_dict = read_dictionary(PRODUCTS_FILE, PRODUCT_NUMBER_INDEX)
    print(len(products_dict))

    # Prints the products_dict
    print("All Products")
    print(products_dict)

    # Opens the request.csv file for reading.
    # Skips the first line of the request.csv file because the first line contains column headings.
    requests_list = read_compound_list(REQUESTS_FILE)

    print("\nRequested Items")
    # Uses a loop that reads and processes each row from the request.csv file.
    for request in requests_list:
        product_number = request[PRODUCT_NUMBER_INDEX]
        requested_quantity = request[QUANTITY_INDEX]
        
        # Use the requested product number to find the corresponding item in the products_dict.
        if product_number in products_dict:
            product = products_dict[product_number]
            product_name = product[PRODUCT_NAME_INDEX]
            product_price = product[RETAIL_PRICE_INDEX]

            # Print the product name, requested quantity, and product price.
            print(f"{product_name}: {requested_quantity} x {product_price}")

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

    # Return the compound list.
    return compound_list

if __name__ == "__main__":
    main()