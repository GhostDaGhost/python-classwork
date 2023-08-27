# Author: Alexander Arizola
# Date: August 27th 2023
# Final Exam - Strings
# This is a program that will return the sum of all the single digits of a social security number provided.

# When triggered, get the sum of a social security number.
# @param socialSecurityNumber `string` - The social security number to calculate the sum for.
# @returns `number` - The sum of all the single digits in the number.
def calculateSumOfSingleDigits(socialSecurityNumber):
    if not socialSecurityNumber or socialSecurityNumber == '': # PARAMETER CHECKS
        print('[calculateSumOfSingleDigits]: You need to enter a valid social security number!')
        return
    
    # ITERATE THROUGH EACH CHARACTER OF THE SOCIAL SECURITY NUMBER
    totalSumOfSingleDigits = 0
    for character in socialSecurityNumber:
        if character.isdigit():
            totalSumOfSingleDigits += int(character)
    
    # RETURN SUM OF SINGLE DIGITS
    return totalSumOfSingleDigits

# When triggered, prompt user for a social security number in order to return the sum.
# No parameters.
# No return value.
def main():
    socialSecurityNumber = input('Enter a Social Security Number (XXX-XX-XXXX): ')
    
    # ENSURE THAT THE PROVIDED SOCIAL SECURITY NUMBER IS VALID
    if not socialSecurityNumber or socialSecurityNumber == '':
        print('[main]: You need to enter a valid social security number!')
        return
    
    # GET SUM OF SINGLE DIGITS FROM THE SOCIAL SECURITY NUMBER
    sumOfSingleDigits = calculateSumOfSingleDigits(socialSecurityNumber)
    print('Sum of Single Digits: ', sumOfSingleDigits)

# TRIGGER THE MAIN FUNCTION WHEN SCRIPT STARTS
main()
