# Author: Alexander Arizola
# Date: August 27th 2023
# A7 - Most Frequent Character 
# This is a program that will manipulate a given string and returns the character that occurs most in the string.

# When triggered, analyze the given string and fetch the most frequent character.
# @param userInput `string` - The string entered by the user.
# @returns `string` - The most frequent character found in the string.
def findFrequentCharacter(userInput):
    if not userInput or userInput == '': # PARAMETER CHECKS
        print('[findFrequentCharacter]: The program ran into a failure with receiving the string.')
        return

    # GET COUNTS OF EACH CHARACTER
    charactersUsed = {}
    for character in userInput:
        if character in charactersUsed:
            charactersUsed[character] += 1
        else:
            charactersUsed[character] = 1

    # FIND THE MOST FREQUENT CHARACTER
    mostFrequentCharacter = ''
    highestCharacterCount = 0

    for character, characterCount in charactersUsed.items():
        if characterCount > highestCharacterCount:
            highestCharacterCount = characterCount
            mostFrequentCharacter = character

    # IF NO POSSIBILITY WAS ABLE TO BE FOUND
    if highestCharacterCount == 1:
        print('No frequent character was found in this string. Please enter a string that would have no ties!')
        return ''

    # RETURN FREQUENT CHARACTER
    return mostFrequentCharacter

# When triggered, ask for the user's input so that we can get a frequent character.
# No parameters.
# No return value.
def main():
    userInput = input('Enter a word: ')

    # CHECK TO MAKE SURE THAT USER'S INPUT IS VALID
    if not userInput or userInput == '':
        print('[main]: You have to enter a valid word. It cannot be blank!')
        return

    # TRIGGER FUNCTION TO FIND THE FREQUENT CHARACTER
    mostFrequentCharacter = findFrequentCharacter(userInput)
    if mostFrequentCharacter and mostFrequentCharacter != '':
        print('The most frequent character in the given string is: ', mostFrequentCharacter)
    
# TRIGGER THE MAIN FUNCTION WHEN SCRIPT STARTS
main()
