# Author: Alexander Arizola
# Date: August 27th 2023
# Final Exam - Modules & Functions
# This is the module to assist with 'stats.py'

# When triggered, get the average value of the provided list
# @param data `list` - The list to get the average value of.
# @returns `number` - The average value of the list.
def get_average(data):
    return sum(data) / len(data)

# When triggered, get the minimum value of the provided list
# @param data `list` - The list to get the minimum value of.
# @returns `number` - The minimum value of the list.
def get_min(data):
    return min(data)

# When triggered, get the below average count of the provided list
# @param data `list` - The list to get the below average count of.
# @returns `number` - The below average count of the list.
def get_below_avg_count(data):
    averageIntegerValue= get_average(data)
    belowAverageCount = sum(1 for value in data if value < averageIntegerValue)
    return belowAverageCount
