# File: 01-Prove_tire_volume
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson01/prove.html
import math

line = "\n*****************************************************\n"
print(f"{line}*    Volume of space inside of a tire calculator    *{line}")

"""
Formula: v = (math.pi * w  ** 2 * a * (w * a + 2540 * d)) / 10000000000

- v is the volume in liters,
- π is the constant PI, which is the ratio of the circumference of a circle divided by its diameter (use math.pi),
- w is the width of the tire in millimeters,
- a is the aspect ratio of the tire, and
- d is the diameter of the wheel in inches.
"""

w = int(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
d = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * w**2 * a * (w * a + 2540 * d)) / 10000000000

print(f"\nThe approximate volume is {volume:.2f} liters")

print(f"{line}*                  Thank you! Bye.                  *{line}")

print(math.pi)