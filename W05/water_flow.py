# File: water_flow.py
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson05/prove.html

def water_column_height(tower_height, tank_height):
    """
    calculates and returns the height of a column of water 
    from a tower height and a tank wall height.

    the following formula for calculating the water column 
    height is: h = t + 3w / 4

    where:
    - h is height of the water column
    - t is the height of the tower
    - w is the height of the walls of the tank that is on top of the tower

    Parameters
        tower_height: a float number
        tank_height: another float number
    Return: a float number
    """

    water_column_height = tower_height + 3 * tank_height / 4
    return water_column_height

def pressure_gain_from_water_height(height):
    """
    calculates and returns the pressure caused by Earth's 
    gravity pulling on the water stored in an elevated tank.

    the formula for calculating pressure caused by Earth's 
    gravity is: P = pgh / 1000

    where:
    - P is the pressure in kilopascals
    - p is the density of water (998.2 kilogram / meter3)
    - g is the acceleration from Earths gravity (9.80665 meter / second2)
    - h is the height of the water column in meters

    Parameters
        height: a float with the height of the water column in meters
    Return: a float number with the pressure in kilopascals
    """
    p = 998.2
    g = 9.80665

    pressure = (p * g * height) / 1000

    return pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """
    calculates and returns the water pressure lost because 
    of the friction between the water and the walls of 
    a pipe that it flows through.

    the following formula for calculating pressure loss from 
    friction within a pipe is: P = -fLpv**2 / 2000d

    where:
    - P is the lost pressure in kilopascals
    - f is the pipe's friction factor
    - L is the length of the pipe in meters
    - p is the density of water (998.2 kilogram / meter3)
    - v is the velocity of the water flowing through the pipe in meters / second
    - d is the diameter of the pipe in meters

    Parameters
        height: a float with the height of the water column in meters
    Return: a float number with the pressure in kilopascals
    """
    p = 998.2
    f = friction_factor * -1
    
    lost_pressure = (f * pipe_length * p * fluid_velocity ** 2) / (2000 * pipe_diameter)
    
    return lost_pressure