# Author: Alex Arizola
# Price Checker

# ASK USER FOR SIZE OF SMALL ITEM
sizeOfSmallItem = input("Enter size of small item (ounces): ")

# ASK USER FOR PRICE OF SMALL ITEM
priceOfSmallItem = input("Enter price of small item: ")

# ASK USER FOR SIZE OF LARGE ITEM
sizeOfLargeItem = input("Enter size of large item (ounces): ")

# ASK USER FOR PRICE OF LARGE ITEM
priceOfLargeItem = input("Enter price of large item: ")

# CALCULATE UNIT PRICE OF BOTH ITEMS
unitPriceOfSmallItem = float(priceOfSmallItem) / int(sizeOfSmallItem)
unitPriceOfLargeItem = float(priceOfLargeItem) / int(sizeOfLargeItem)

# DEBUG
print("unitPriceOfSmallItem", unitPriceOfSmallItem)
print("unitPriceOfLargeItem", unitPriceOfLargeItem)

# DETERMINE WHICH ITEM IS THE BEST IN THE DEAL
if unitPriceOfLargeItem < unitPriceOfSmallItem:
    print("The large item is the better deal!")
else:
    print("The small item is the better deal!")
