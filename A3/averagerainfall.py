# Author: Alexander Arizola
# A3 - Average Rainfall
# This is a program that will calculate the average rainful over a period of years.

# FIRSTLY, ASK THE USER TO INPUT THE AMOUNT OF YEARS THEY WANT TO CALCULATE
totalYears = int(input('Please enter the amount of years: '))

# ENSURE THAT THE USER'S INPUT IS A POSITIVE NUMBER
while totalYears <= 0:
    totalYears = int(input(
        'There was an error with your previously inputted amount of years.'
        +
        ' Please enter the amount of years again: '
    ))

    if type(totalYears) == 'int' and totalYears >= 1:
        break

# SECONDLY, ITERATE THROUGH THE AMOUNT OF YEARS THAT THE USER INPUTTED
print("**********************")

totalInchesOfRainfall = 0.00
for year in range(totalYears):
    year = year + 1 # TOTAL YEARS GETS OFFSET IN THE ITERATION BY -1

    for month in range(1, 13): # SET TO 13 DUE TO OFFSET BY -1
        rainfallForThisMonth = float(input('Enter the rainfall for year '+ str(year) +', month '+ str(month) +': '))
        totalInchesOfRainfall += rainfallForThisMonth

print("**********************")

# FINALLY, LET'S PRINT THE RESULTS AND SUM OF RAINFALL AND MONTHS
totalNumberOfMonths = 12 * totalYears
print("Number of months: "+ str(totalNumberOfMonths) +", Total rainfall in inches: "+ str(totalInchesOfRainfall) +", Average rainfall: " + format(totalInchesOfRainfall / totalNumberOfMonths, '.2f'))
