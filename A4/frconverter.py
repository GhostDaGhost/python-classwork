# Author: Alexander Arizola
# A4 - Fahrenheit to Reaumur Converter Function
# This is a program that will convert a Fahrenheit temperature value to Reaumur.

# WHEN TRIGGERED, THIS WILL ASK THE USER TO INPUT A FAHRENHEIT TEMPERATURE VALUE FOR CONVERSION LATER
# No parameters
# No return value
def OnProgramExecution():
    fahrenheitInput = int(input('Enter a temperature in fahrenheit: ')) # ASK FOR INPUT

    # FEEDBACK PRINT AND CHECK IF IT IS VALID
    print('[OnProgramExecution]: You have entered a fahrenheit temperature of: ', str(fahrenheitInput))
    if fahrenheitInput and fahrenheitInput > 0:
        FR_converter(fahrenheitInput)
    else:
        print('[OnProgramExecution]: You did not enter a correct input! Please try again.')

# WHEN TRIGGERED, THIS WILL CONVERT AN INPUTTED FAHRENHEIT TEMPERATURE VALUE INTO REAUMUR
# @param fahrenheitToConvert {int} - The fahrenheit temperature to convert into reaumur
# @return reaumurResult {str} - The converted temperature in reaumur
def FR_converter(fahrenheitToConvert):
    if not fahrenheitToConvert or fahrenheitToConvert <= 0: # PARAMETER CHECK
        return print('[FR_converter]: Did not receive a valid parameter. Please try again!')

    # CONVERT FAHRENHEIT INTO REAUMUR
    reaumurResult = format((fahrenheitToConvert - 32) * (4 / 9), '.2f')
    print('[FR_converter]: Reaumur: ', reaumurResult)

    # RETURN CONVERTED VALUE
    return reaumurResult

# TRIGGER THE MAIN FUNCTION UPON PROGRAM EXECUTION
OnProgramExecution()
