# Author: Alexander Arizola
# Part 2: Multi-way Structures - Shipping Charges

# FIRST, ASK THE USER TO ENTER THE WEIGHT OF THEIR PACKAGE
packageWeightInput = int(input('Enter the weight of your package '))

# SECONDLY, START CALCULATING THE COST OF THE SHIPPING WITH RATE AND WEIGHT
shippingCost = 0.00
if packageWeightInput <= 2:
    shippingCost = 1.10 * packageWeightInput
    print('Applying $1.10 rate to cost calculation.')
elif packageWeightInput > 2 and packageWeightInput < 7:
    shippingCost = 2.20 * packageWeightInput
    print('Applying $2.20 rate to cost calculation.')
elif packageWeightInput > 6 and packageWeightInput < 10:
    shippingCost = 3.70 * packageWeightInput
    print('Applying $3.70 rate to cost calculation.')
elif packageWeightInput > 10:
    shippingCost = 3.80 * packageWeightInput
    print('Applying $3.80 rate to cost calculation.')
    
# FINALLY, PRINT THE COST OF SHIPPING THE PACKAGE
print('The cost of shipping this package ('+ str(packageWeightInput) +' lbs) will be $%.2f' % shippingCost)
