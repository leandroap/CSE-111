# Example 3 - Reference: https://byui-cse.github.io/cse111-course/lesson11/prepare.html

''''
Nested Functions
The Python programming language allows a programmer to define nested functions. 
A nested function is a function that is defined inside another function and is useful when 
we wish to split a large function into smaller functions and the smaller functions will 
be called by the containing function only. 
The program in example 3 produces the same results as examples 1 and 2, 
but it uses a nested function. Notice in example 3 at lines 5–10 that the cels_from_fahr 
function is nested inside the main function.
'''

def main():

    def cels_from_fahr(fahr):
        """Convert a Fahrenheit temperature to
        Celsius and return the Celsius temperature.
        """
        cels = (fahr - 32) * 5 / 9
        return round(cels, 1)

    fahr_temps = [72, 65, 71, 75, 82, 87, 68]

    # Print the Fahrenheit temperatures.
    print(f"Fahrenheit: {fahr_temps}")

    # Convert each Fahrenheit temperature to Celsius and store
    # the Celsius temperatures in a list named cels_temps.
    cels_temps = list(map(cels_from_fahr, fahr_temps))

    # Print the Celsius temperatures.
    print(f"Celsius: {cels_temps}")


# Call main to start this program.
if __name__ == "__main__":
    main()