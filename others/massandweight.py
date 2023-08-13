# Author: Alexander Arizola
# Midterm - Mass and Weight
# This is a program that will display the indicator of an object's weight.

# Ask user for the mass of the object.
objectMass = float(input('Please enter the mass of the object: '))
if objectMass and objectMass > 0:
    objectWeight = objectMass * 9.8 # Calculate the weight of the object using its mass.

    # Start condition checks in order to get the correct message.
    if objectWeight < 10:
        print('The object is too LIGHT in weight.')
    elif objectWeight > 100:
        print('The object is too HEAVY in weight.')
    else:
        print('The object is at a normal weight.')
else:
    print('Please enter a valid number.')
