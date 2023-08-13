# Author: Alexander Arizola
# Midterm - Celsius to Fahrenheit Table
# This is a program that will display a table of Celsius temperatures from 0 through 20 and their Fahrenheit equivalents.

# Start by printing out the columns
print('Celsius', '  Fahrenheit')

# Iterate through Celsius temperatures from 0 to 20.
for celsiusTemperature in range(21): # 21 is needed due to a -1 offset. It will loop until 20. 
    fahrenheitTemperature = (celsiusTemperature * 9 / 5) + 32 # Calculate the Fahrenheit temperature from Celsius.

    # Display the celsius temperature and the Fahrenheit equivalent.
    print(celsiusTemperature, '       ', int(fahrenheitTemperature))