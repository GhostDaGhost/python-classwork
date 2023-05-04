# Author: Alex Arizola
# Program 2 / Temperature Converter

import math

# ASK USER FOR FAHRENHEIT
fahrenheit = int(input("Enter fahrenheit: "))

# CONVERT FAHRENHEIT INTO KELVIN
kelvin = (fahrenheit + 459.67) * 5/9

# OUTPUT THE CONVERTED INPUT
print("Kelvin:", math.floor(kelvin))
