# Author: Alex Arizola
# Practice | 6/1/2022
# Program / Dictionary, Function practice

months = { # DICTIONARY OF MONTHS AND DAYS WITHIN EACH
    # Month Name: ['Month Number, Number of Days In Month],
    "January": ['1', 31],
    "February": ['2', 28],
    "March": ['3', 31],
    "April": ['4', 30],
    "May": ['5', 31],
    "June": ['6', 30],
    "July": ['7', 31],
    "August": ['8', 31],
    "September": ['9', 30],
    "October": ['10', 31],
    "November": ['11', 30],
    "December": ['12', 31]
}

# WHEN TRIGGERED, ASK USER FOR MONTH OF THE YEAR
def AskUserForMonth():
    monthInput = input('Enter a month of the year: ')
    
    if monthInput != '':
        print('You have entered a month of', monthInput)

        if monthInput in months: # CHECK IF INPUT IS A MONTH NAME
            print('This is a month of the year! Here are the days of this month:', months[monthInput][1])
        else: # CHECK IF INPUT IS A MONTH NUMBER
            # FIND THE MONTH ASSOCIATED WITH THE NUMBER
            for monthName, monthData in months.items():
                if monthData[0] == monthInput:
                    return print(monthName, 'is a month of the year! Here are the days of this month:', monthData[1])

            # IN THE END, WE COULD NOT FIND THIS MONTH
            print('[ERROR]: This is not a month of the year!')
    else:
        print('You did not enter a correct month input!')

# TRIGGERS UPON SCRIPT EXECUTION
AskUserForMonth()
