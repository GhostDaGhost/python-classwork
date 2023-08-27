# Author: Alexander Arizola
# Date: August 27th 2023
# A7 - Pig Latin
# This is a program that will manipulate a given string to convert each word to "Pig Latin".

# When triggered, analyze the given string and convert it to pig latin.
# @param sentenceToConvert `string` - The string entered by the user.
# @returns `string` - The converted sentence in pig latin.
def convertSentenceToPigLatin(sentenceToConvert):
    sentenceList = sentenceToConvert.split()
    convertedSentence = ''

    # ITERATE THROUGH THE WORDS IN THE SENTENCE TO MANIPULATE IT
    for word in sentenceList:
        convertedSentence += word[1:] + word[0] + 'ay '

    # RETURN THE NEWLY CONVERTED SENTENCE
    return convertedSentence

# When triggered, ask for the user's input so that we can convert it.
# No parameters.
# No return value.
def main():
    sentenceToConvert = input('Enter a sentence to convert: ')

    # CHECK TO MAKE SURE THAT USER'S INPUT IS VALID
    if not sentenceToConvert or sentenceToConvert == '':
        print('[main]: You have to enter a valid sentence. It cannot be blank!')
        return

    # TRIGGER FUNCTION TO CONVERT SENTENCE TO PIG LATIN
    convertedSentence = convertSentenceToPigLatin(sentenceToConvert)
    if convertedSentence and convertedSentence != '':
        print('English: ', sentenceToConvert)
        print('Pig Latin: ', convertedSentence)
    
# TRIGGER THE MAIN FUNCTION WHEN SCRIPT STARTS
main()
