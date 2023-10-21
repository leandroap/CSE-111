# File: water_flow.py
# Author: Leandro Amaral Pereira
# Reference: https://byui-cse.github.io/cse111-course/lesson05/prove.html

def water_column_height(tower_height, tank_height):
    """
    calculates and returns the height of a column of water 
    from a tower height and a tank wall height.

    the formula for calculating the water column 
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
    - g is the acceleration from Earths gravity (9.80665 meter / second**2)
    - h is the height of the water column in meters

    Parameters
        height: a float with the height of the water column in meters
    Return: a float number with the pressure in kilopascals
    """
    p = WATER_DENSITY
    g = EARTH_ACCELERATION_OF_GRAVITY

    pressure = (p * g * height) / 1000

    return pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """
    calculates and returns the water pressure lost because 
    of the friction between the water and the walls of 
    a pipe that it flows through.

    the formula for calculating pressure loss from 
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
    p = WATER_DENSITY
    lost_pressure = (-friction_factor * pipe_length * p * fluid_velocity ** 2) / (2000 * pipe_diameter)
    
    return lost_pressure

def pressure_loss_from_fittings(fluid_velocity, 
                                quantity_fittings):
    """
    calculates and returns the the water pressure lost 
    because of fittings such as 45° and 90° bends that are in a pipeline.

    the formula for calculating pressure loss from pipe fittings 
    is: P = -0.04 p v**2 n / 2000

    where:
    - P is the lost pressure in kilopascals
    - p is the density of water (998.2 kilogram / meter3)
    - v is the velocity of the water flowing through the pipe in meters / second
    - n is the quantity of fittings

    Parameters
        fluid_velocity: a float with the velocity of the water 
            flowing through the pipe
        quantity_fittings: an integer with the quantity of fittings
    Return: a float number with the pressure in kilopascals
    """

    p = WATER_DENSITY
    pressure = (-0.04 * p * fluid_velocity ** 2 * quantity_fittings) / 2000
    
    return pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    calculates and returns the Reynolds number for a pipe 
    with water flowing through it.

    the formula for calculating the Reynolds number 
    is: R = pdv / μ

    where:
    - R is the Reynolds number
    - p is the density of water (998.2 kilogram / meter3)
    - d is the hydraulic diameter of a pipe in meters. 
        For a round pipe, the hydraulic diameter is the 
        same as the pipe's inner diameter.
    - v is the velocity of the water flowing through 
        the pipe in meters / second
    - μ is the dynamic viscosity of water (0.0010016 Pascal seconds)

    Parameters
        hydraulic_diameter: a float with the hydraulic diameter of a pipe
        fluid_velocity: a float with the velocity of the water flowing through the pipe
    Return: a number with the Reynolds number
    """

    p = WATER_DENSITY
    mu = WATER_DYNAMIC_VISCOSITY
    R = (p * hydraulic_diameter * fluid_velocity) / mu

    return R

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    """
    calculates and returns the water pressure lost because 
    of water moving from a pipe with a large diameter 
    into a pipe with a smaller diameter.

    the formula for calculating pressure loss from a rounded 
    reduction in a pipe's diameter are: 
    k = (0.1 + 50/R) * ((D/d)**4 - 1)
    P = -kpv**2 / 2000


    where:
    - k is a constant computed by the first formula and used in 
        the second formula
    - R is the Reynolds number that corresponds to the pipe with 
        the larger diameter
    - D is the diameter of the larger pipe in meters
    - d is the diameter of the smaller pipe in meters
    - P is the lost pressure kilopascals
    - p is the density of water (998.2 kilogram / meter3)
    - v is the velocity of the water flowing through the 
        larger diameter pipe in meters / second

    Parameters
        larger_diameter: a float with the diameter of the larger pipe
        fluid_velocity: a float with the velocity of the water 
            flowing through the pipe
        reynolds_number: a number with the Reynolds number
        smaller_diameter: a float with the diameter of the smaller pipe
        
    Return: a float number with the lost pressure in kilopascals
    """

    p = WATER_DENSITY
    k = (0.1 + 50/reynolds_number) * ((larger_diameter/smaller_diameter)**4 - 1)
    P = (-k * p * (fluid_velocity**2)) / 2000

    return P

def psi_from_kpa(kpa):
    """
    converts water pressure in kilopascals (kPa) to pounds per square inch (psi)

    Parameters
        kpa: a float number with the kPa
    
    Return: a float number with the psi
    """

    psi = kpa * 0.1450377377

    return psi

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)

EARTH_ACCELERATION_OF_GRAVITY = 9.80665 # meter / second**2
WATER_DENSITY = 998.2                   # kilogram / meter**3
WATER_DYNAMIC_VISCOSITY = 0.0010016     # Pascal seconds

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f"Pressure at house: {psi_from_kpa(pressure):.1f} psi")

# If this file was executed like this:
# > python water_flow.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()