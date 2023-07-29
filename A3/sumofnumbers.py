# Author: Alexander Arizola
# A3 - Sum of Numbers
# This is a program that will sum a series of positive numbers entered through input until a negative number is inputted.

# FIRSTLY, LET'S INFORM THE USER THAT THE LOOP CAN BE ENDED BY ENTERING A NEGATIVE NUMBER
print("You may end the loop at any time by entering a negative number.")

# SECONDLY, ASK USER FOR A POSITIVE NUMBER
sumOfNumbers = 0
numberToAdd = int(input("Enter a positive number: "))

# START A LOOP TO CONTINUOUSLY ASK FOR A POSITIVE NUMBER UNTIL A NEGATIVE NUMBER IS GIVEN
while numberToAdd >= 0:
    sumOfNumbers += numberToAdd
    numberToAdd = int(input("Enter a positive number: "))

# ONCE THE LOOP IS TERMINATED, PRINT THE SUM TO THE CONSOLE
print("The sum of positive numbers is:", sumOfNumbers)
