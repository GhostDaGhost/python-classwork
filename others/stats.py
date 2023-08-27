# Author: Alexander Arizola
# Date: August 27th 2023
# Final Exam - Modules & Functions
# This is a program that will prompt the user for 10 integer values and then triggers select functions

# Import 'funcbundle' module
import funcbundle

# When triggered, prompt user for 10 integer values and then start trigger functions
# No parameters.
# No return value.
def main():
    integerValues = []

    # ITERATE 10 TIMES TO GET INPUT FOR EACH ITERATION
    for times in range(10):
        integerValue = input(f'Enter the integer value for #{times + 1}: ')
        
        # CHECK IF THE INTEGER VALUE IS VALID
        if not integerValue or integerValue == '':
            return 'You need to enter a valid integer value!'
        
        # APPEND TO LIST
        integerValues.append(int(integerValue))

    # GET AVERAGE OF VALUES
    averageIntegerValue = funcbundle.get_average(integerValues)
    minimumIntegerValue = funcbundle.get_min(integerValues)
    belowAverageCount = funcbundle.get_below_avg_count(integerValues)

    # OUTPUT ALL VALUES
    print('Entered Integer Values: ', integerValues)
    print(f'Average Value: {averageIntegerValue:.2f}')
    print('Smallest Value: ', minimumIntegerValue)
    print('Below Average Count: ', belowAverageCount)

# TRIGGER THE MAIN FUNCTION WHEN SCRIPT STARTS
main()
