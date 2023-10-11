# File: 02-Prove_tire_volume
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson02/prove.html

"""
Formula: v = (math.pi * w  ** 2 * a * (w * a + 2540 * d)) / 10000000000

- v is the volume in liters,
- π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
- w is the width of the tire in millimeters,
- a is the aspect ratio of the tire, and
- d is the diameter of the wheel in inches.
"""
import math
from datetime import datetime

# Function to print some decorative elements
def print_elements(option): 
    break_line = "\n*****************************************************\n"
    header       = "*    Volume of space inside of a tire calculator    *"
    footer       = "*                  Thank you! Bye.                  *"

    if option == "header":
        print(f"{break_line}{header}{break_line}")
    elif option == "footer":
        print(f"{break_line}{footer}{break_line}")

print_elements("header")

#prompt for three numbers and converts all three numbers
w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

#calculate tire volume
volume = (math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000

#prints the volume
print(f"\nThe approximate volume is {volume:.2f} liters\n")

#Exceeding the Requirements
no = "\u0332".join("no)")
wants_to_buy = input(f"Do you want to buy tires with that dimensions? (yes/{no}: " or "no")
phone = ""

if wants_to_buy.lower() == "yes":
    phone = input("Enter your phone number: ")

#Gets and format the current date from the computer’s operating system.
current_date_time = f"{datetime.now():%Y-%m-%d}"

#Prepare data to append into file
log_info = f"{current_date_time}, {w}, {a}, {d}, {volume:.2f}, {phone}"

#Opens a text file named volumes.txt for appending.
with open("volumes.txt", mode="at") as volumes_file:
    #Appends the width, aspect ratio, diameter, and volume to the volumes.txt file
    print(log_info, file=volumes_file)

print_elements("footer")