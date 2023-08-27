# Author: Alexander Arizola
# Date: August 27th 2023
# Final Exam - Dictionaries
# This is a program that will calculate and display the total rainfall of a year as well as monthly stats.

# When triggered,
# No parameters.
# No return value.
def main():
    rainfallMonths = {}

    # ITERATE THROUGH 12 MONTHS AND HAVE USER INPUT THE MONTH AND AMOUNT OF RAINFALL
    for month in range(12):
        monthName = input('Please enter the month name: ')

        # ENSURE THAT THE MONTH WASN'T ALREADY INPUTTED
        if monthName in rainfallMonths:
            print('You have already entered: ', monthName)
            return
        
        # ADD TO THE DICTIONARY FOR MONTHS
        monthRainfall = float(input(f'Please enter the rainfall amount for {monthName}: '))
        rainfallMonths[monthName] = monthRainfall

    # GET TOTAL AND AVERAGE RAINFALL
    totalAnnualRainfall = sum(rainfallMonths.values())
    averageMonthlyRainfall = totalAnnualRainfall / len(rainfallMonths)

    # GET LOWEST AND HIGHEST MONTHS IN TERMS OF RAINFALL
    lowestRainfallMonth = min(rainfallMonths, key = rainfallMonths.get)
    highestRainfallMonth = max(rainfallMonths, key = rainfallMonths.get)

    # OUTPUT ALL VALUES GAINED
    print('Total Annual Rainfall: ', format(totalAnnualRainfall, '.2f'))
    print('Average Monthly Rainfall: ', format(averageMonthlyRainfall, '.2f'))
    print('Month with Highest Rainfall: ', highestRainfallMonth)
    print('Month with Lowest Rainfall: ', lowestRainfallMonth)

# TRIGGER THE MAIN FUNCTION WHEN SCRIPT STARTS
main()
