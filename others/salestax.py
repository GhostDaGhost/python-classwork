# Author: Alexander Arizola
# Midterm - Sales Tax
# This is a program that will display the amount of the purchase, the state sales tax, the county sales tax, the total sales tax, and the total of the sale.

# Variables to represent tax percentages
stateSalesTax = 0.04
countySalesTax = 0.02

# Ask user for amount of purchase through input
amountOfPurchase = float(input('Please enter the amount of a purchase: '))
if (amountOfPurchase and amountOfPurchase > 0):
    # Display the original purchase price
    print('Original Price: $', amountOfPurchase)

    # Apply taxes to the original purchase price
    stateSalesTaxedPrice = amountOfPurchase * stateSalesTax
    countySalesTaxedPrice = amountOfPurchase * countySalesTax

    # Display each tax applied
    print('State Tax: $', format(stateSalesTaxedPrice, '.2f'))
    print('County Tax: $', format(countySalesTaxedPrice, '.2f'))

    # Sum the tax that was applied to the original purchase price
    totalSalesTax = stateSalesTaxedPrice + countySalesTaxedPrice
    print('Total Sales Tax: $', format(totalSalesTax, '.2f'))

    # Sum the sale with all the taxes applied
    totalSalesPrice = amountOfPurchase + totalSalesTax
    print('Total Sales Price: $', format(totalSalesPrice, '.2f'))
else:
    print('Please enter a valid number.')
