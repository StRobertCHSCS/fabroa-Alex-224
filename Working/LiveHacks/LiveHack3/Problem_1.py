'''
-------------------------------------------------------------------------------
Name:		problem_1.py
Purpose:	calculate number of heating days

Author:	Yu.A

Created:	December 9 2019
------------------------------------------------------------------------------
'''

#get number of days to check temperature from user
number_of_days = int(input("Enter the number of days to track: "))

#get temperatures from user and calculate heating days
heating_days = 0
for i in range(number_of_days):
    temperatures = input()
    if int(temperatures) >= 15:
        heating_days = heating_days + 1
print("There are ", heating_days,"heating days")