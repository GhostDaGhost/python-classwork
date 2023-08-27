# Author: Alexander Arizola
# Date: August 27th 2023
# Final Exam - Lists
# This is a program that will produce the fair average score from 10 competition scores from 0-10.

# When triggered, produce the fair average score of 10 competition scores.
# No parameters.
# No return value.
def main():
    competitionScores = [8, 5, 9, 3, 7, 2, 6, 4, 10, 1]

    # GET LOWEST SCORE AND PRINT IT ALONG WITH THE POSITION
    lowestScore = min(competitionScores)
    lowestScorePosition = competitionScores.index(lowestScore)
    print(f'The first lowest score is {lowestScore} located at position {lowestScorePosition}')

    # REMOVE LOWEST SCORE FROM THE LIST
    competitionScores.pop(lowestScorePosition)

    # GET HIGHEST SCORE AND PRINT IT ALONG WITH THE POSITION
    highestScore = max(competitionScores)
    highestScorePosition = competitionScores.index(highestScore)
    print(f'The first highest score is {highestScore} located at position {highestScorePosition}')

    # GET AVERAGE SCORE AND PRINT IT
    averageScore = sum(competitionScores) / len(competitionScores)
    print(f'The effective score is {averageScore}')

# TRIGGER THE MAIN FUNCTION WHEN SCRIPT STARTS
main()
