# Author: Alexander Arizola
# A4 - Cone Volume Function
# This is a program that will calculate and display the volume of a cone with an inputted height and base radius.

# IMPORTS MATH FUNCTIONS
import math

# WHEN TRIGGERED, THIS WILL CALCULATE THE VOLUME OF A CONE WITH PARAMETERS OF HEIGHT AND RADIUS
# @param height - int - The height to calculate with.
# @param radius - int - The base radius to calculate with.
# @returns calculatedConeVolume - int - The calculated volume of the cone.
def coneVolume(height, radius):
    calculatedConeVolume = math.pi * (radius * radius) * height / 3

    # OUTPUT THE VOLUME OF THE CONE TO THE CONSOLE
    print("The volume of the cone is: " + str(calculatedConeVolume))
    return calculatedConeVolume

# WHEN TRIGGERED, THIS WILL BE TRIGGERED UPON PROGRAM EXECUTION AND ASKS FOR HEIGHT AND BASE RADIUS THROUGH INPUT
# No parameters.
# This returns nothing.
def main():
    heightInput = int(input("Please enter the height of the cone: "))

    # VALIDATE HEIGHT INPUT
    if (heightInput and heightInput > 0):
        baseRadiusInput = int(input("Please enter the base radius of the cone: "))
        
        # VALIDATE BASE RADIUS INPUT
        if (baseRadiusInput and baseRadiusInput > 0):
            coneVolume(heightInput, baseRadiusInput)
        else:
            print("Please enter a valid base radius.")
    else:
        print("Please enter a valid height.")

# TRIGGERS WHEN PROGRAM IS EXECUTED
main()
