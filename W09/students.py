
import csv

def main():
    NUMBER_INDEX = 0
    NAME_INDEX = 1

    student_dictionary = read_dictionary("students.csv", NUMBER_INDEX)
    
    do_again = "yes"

    while do_again == "yes":
        i_number = input("Please enter an I-Number (xxxxxxxxx): ").replace("-", "")

        if is_valid(i_number):
            if i_number in student_dictionary:
                student = student_dictionary[i_number]

                print(student[NAME_INDEX])
            else:
                print("No such student")

        do_again = input("Do you want to seek another student? (yes/no): ").lower()

def is_valid(i_number):
    is_valid = False

    if i_number.isnumeric() == False:
        print("Invalid I-Number")
    elif len(i_number) < 9:
        print("Invalid I-Number: too few digits")
    elif len(i_number) > 9:
        print("Invalid I-Number: too many digits")
    else:
        is_valid = True

    return is_valid

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

if __name__ == "__main__":
    main()