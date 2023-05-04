# Author: Alex Arizola
# Program 2 / Cone Volume Function

pie = 3.14285714286

# WHEN TRIGGERED, CONVERT HEIGHT AND RADIUS TO VOLUME
def ConvertHeightRadiusToVolume(heightInput, radiusInput):
    volume = pie * (radiusInput * radiusInput) * heightInput / 3  
    print("Converted Volume: " + str(volume))

# WHEN TRIGGERED, ASK USER FOR HEIGHT AND RADIUS
def AskUserForHeightRadius():
    heightInput = input('Enter a height: ')
    
    if heightInput != '':
        print('You have entered a height of ', heightInput)

        radiusInput = input('Enter a radius: ')
        if radiusInput != '':
            print('You have entered a radius of ', radiusInput)
            ConvertHeightRadiusToVolume(int(heightInput), int(radiusInput))
        else:
            print('You did not enter a correct height input!')
    else:
        print('You did not enter a correct height input!')


# TRIGGERS UPON SCRIPT EXECUTION
AskUserForHeightRadius()
