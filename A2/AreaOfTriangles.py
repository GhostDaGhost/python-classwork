# Author: Alexander Arizola
# Part 1: Decision Structures - Area of Triangles

##############
# TRIANGLE ONE
##############
# FIRST, ASK THE USER TO ENTER BASE
triangleOneBaseInput = int(input('Enter base for triangle #1: '))

# NEXT, ASK THE USER TO ENTER HEIGHT
triangleOneHeightInput = int(input('Enter height for triangle #1: '))

# CALCULATE AREA OF THE TRIANGLE
areaOfTriangleOne = (triangleOneBaseInput * triangleOneHeightInput) / 2

##############
# TRIANGLE TWO
##############
# FIRST, ASK THE USER TO ENTER BASE
triangleTwoBaseInput = int(input('Enter base for triangle #2: '))

# NEXT, ASK THE USER TO ENTER HEIGHT
triangleTwoHeightInput = int(input('Enter height for triangle #2: '))

# CALCULATE AREA OF THE TRIANGLE
areaOfTriangleTwo = (triangleTwoBaseInput * triangleTwoHeightInput) / 2

##############
# CONCLUSION
##############
# COMPARE AREA OF TRIANGLES AND DETERMINE WHICH ONE IS GREATER OR IF THEY ARE EQUAL
if areaOfTriangleOne == areaOfTriangleTwo:
    print('Both triangles share the same area.')
elif areaOfTriangleOne > areaOfTriangleTwo:
    print('Triangle #1 has the greatest area.')
elif areaOfTriangleOne < areaOfTriangleTwo:
    print('Triangle #2 has the greatest area.')
else:
    print('Error in calculation. Please review the code.')
