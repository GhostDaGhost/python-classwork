# Author: Alex Arizola
# Grade Tracker

import math

# ASK FOR GRADE THAT THE USER WANT'S TO ACHIEVE
desiredGrade = float(input("Enter a decimal grade that you want to achieve (example: 3.5): "))

# COMPARE
if desiredGrade < 2.0 or desiredGrade > 4.0:
    print("Desired grade is not in range! Try again.")
else:
    # ASK FOR OVERALL PERCENTAGE FOR THE CLASS
    currentOverallPercentage = float(input("Enter your overall percentage for the class (example: 85.4): "))

    if currentOverallPercentage < 0 or currentOverallPercentage > 110:
        print("Current overall percentage is not in range! Try again.")
    else:
        desiredGrade = math.floor(float(currentOverallPercentage) / 10.0 - 5.5)

        # DEBUG
        print("desiredGrade", desiredGrade)

        if 1: # THIS WILL ALWAYS RETURN THIS PRINT
            print("Congrats! You are on track to make your target grade")
        else:
            print("Oops. You need to work harder to make your target grade")
