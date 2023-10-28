# File: random_numbers.py
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson07/teach.html

import random
def main():

    # Creates a list named numbers
    numbers = [16.2, 75.1, 52.3]
    
    # Prints the numbers list
    print(f"numbers - step 1: {numbers}")

    # Calls the append_random_numbers function with only 
    # one argument to add one number to numbers
    append_random_numbers(numbers)
    # Prints the numbers list
    print(f"numbers - step 2: {numbers}")

    # Calls the append_random_numbers function again 
    # with two arguments to add three numbers to numbers
    append_random_numbers(numbers, 3)
    # Prints the numbers list
    print(f"numbers - step 3: {numbers}")

    # Creates a list named words
    words = []

    append_random_words(words)
    print(f"words - step 1: {words}")
    
    append_random_words(words, 2)
    print(f"words - step 2: {words}")
    
    append_random_words(words, 3)
    print(f"words - step 3: {words}")


def append_random_numbers(numbers_list, quantity=1):

    for i in range(quantity):
        number = round(random.uniform(1, 99), 1)
        numbers_list.append(number)

def append_random_words(words_list, quantity=1):
    options = ['join', 'love', 'smile', 'cat', 'cloud', 'head', 'dog', 'star', 'green']

    for i in range(quantity):
        words_list.append(random.choice(options))

# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()