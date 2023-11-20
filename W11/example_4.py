# Example 4 - Reference: https://byui-cse.github.io/cse111-course/lesson11/prepare.html

''''
Lambda Functions
A Python lambda function is a small anonymous function, meaning a small function without a name. 
A lambda function is always a small function because the Python language restricts a lambda 
function to just one expression. 
Consider the program in example 4 which is yet another example program that converts 
Fahrenheit temperatures to Celsius. 
Notice the lambda function at line 12 of example 4. 
It takes one parameter named fahr and computes and returns the corresponding Celsius temperature. 
At line 16, the lambda function is passed into the map function.
'''

def main():
    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Define a lambda function that converts
    # a Fahrenheit temperature to Celsius and
    # returns the Celsius temperature.
    # cels_from_fahr = lambda fahr: round((fahr - 32) * 5 / 9, 1)

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    # cels_temps = list(map(cels_from_fahr, fahr_temps))

    ''''
    Some students are confused by the statement that a lambda function is an anonymous function 
    (a function without a name). Looking at the lambda function in example 4 at line 12, 
    it appears that the lambda function is named cels_from_fahr. However, cels_from_fahr is the 
    name of a variable, not the name of the lambda function. The lambda function has no name. 
    This distinction may seem trivial until we see an example of an inline lambda function. 
    Notice in the next example that the lambda function is defined inside the parentheses for 
    the call to the map function.
    '''

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(
            lambda fahr: round((fahr - 32) * 5 / 9, 1),
            fahr_temps))


    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


# Call main to start this program.
if __name__ == "__main__":
    main()

