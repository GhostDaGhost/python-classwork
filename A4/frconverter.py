# Author: Alex Arizola
# Program 1 / Fahrenheit to Reaumur Converter

# WHEN TRIGGERED, CONVERT THE FAHRENHEIT INPUT TO REAUMUR 
def ConvertFahrenheitToReaumur(fahrenheitInput):
    if fahrenheitInput == '': # PARAMETER CHECK
        return print('[ConvertFahrenheitToReaumur]: Did not receive a valid parameter.')

    # CONTINUE THE FUNCTION
    reaumurResult = (fahrenheitInput - 32) * (4 / 9)
    print('Reaumur: ', reaumurResult)

# WHEN TRIGGERED, ASK USER FOR FAHRENHEIT THEY'D LIKE TO CONVERT
def AskUserForFahrenheit():
    fahrenheitInput = input('Enter a temperature in fahrenheit: ')
    
    print('You have entered: ', fahrenheitInput)
    if fahrenheitInput != '':
        ConvertFahrenheitToReaumur(int(fahrenheitInput))
    else:
        print('You did not enter a correct input!')


# TRIGGERS UPON SCRIPT EXECUTION
AskUserForFahrenheit()
