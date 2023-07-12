# Author: Alexander Arizola
# Program 3 / Trapezoidal Prism Volume

# FIRST, ASK THE USER TO ENTER LENGTH
lengthInput = int(input('Enter length: '))

# NEXT, ASK THE USER TO ENTER HEIGHT
heightInput = int(input('Enter height: '))

# NEXT, ASK THE USER TO ENTER BASE WIDTH
baseWidthInput = int(input('Enter base width: '))

# NEXT, ASK THE USER TO ENTER TOP WIDTH
topWidthInput = int(input('Enter top width: '))

# CALCULATE THE VOLUME
volumeOfPrism = lengthInput * heightInput * ((baseWidthInput + topWidthInput) / 2)

# OUTPUT MEASUREMENTS AND VOLUME
print("Here are the un-modified measurements and volume:")
print("Length", lengthInput)
print("Height", heightInput)
print("Base Width", baseWidthInput)
print("Top Width", topWidthInput)
print("Volume:", volumeOfPrism)
print("-=-=-=-=-=-=-=-")

# REDUCE ALL MEASUREMENTS BY 25%
reducedLengthInput = lengthInput / 25
reducedHeightInput = heightInput / 25
reducedBaseWidthInput = baseWidthInput / 25
reducedTopWidthInput = topWidthInput / 25

# CALCULATE REDUCED VOLUME
reducedVolumeOfPrism = reducedLengthInput * reducedHeightInput * ((reducedBaseWidthInput + reducedTopWidthInput) / 2)

# OUTPUT REDUCED MEASUREMENTS AND VOLUME
print("Here are the reduced measurements and volume:")
print("Reduced Length", reducedLengthInput)
print("Reduced Height", reducedHeightInput)
print("Reduced Base Width", reducedBaseWidthInput)
print("Reduced Top Width", reducedTopWidthInput)
print("Reduced Volume:", reducedVolumeOfPrism)
