# File: 01-Check_heart_rate.py
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson01/check.html

"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

age = int(input("Please enter your age: "))
max_rate = 220 - age
slowest_rate = max_rate * 0.65
fastest_rate = max_rate * 0.85

msg = "When you exercise to strengthen your heart, you should\nkeep your heart rate between"
print(f"{msg} {int(slowest_rate)} and {int(fastest_rate)} beats per minute.")


