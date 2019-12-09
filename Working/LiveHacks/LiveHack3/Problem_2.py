'''
-------------------------------------------------------------------------------
Name:		problem_2.py
Purpose:	calculate number of days taken to drive 100km and average distance

Author:	Yu.A

Created:	December 9 2019
------------------------------------------------------------------------------
'''

#get distance travelled and calculate until reaches 100km
number_of_days = 0 
i = 0
while i < 100:
    distance = int(input("enter the distance you travelled for the day(km) "))
    i = i + distance
    number_of_days = number_of_days + 1
print("it took you", number_of_days, "to surpass 100km driven")

#calculate average distance driven
average = i/number_of_days
print("the average distance driven per day is", average, "km")