'''
-------------------------------------------------------------------------------
Name:		problem 2_1.py
Purpose:	calculate bmi and weight classification of user

Author:	Yu.A

Created:	november 18 2019
------------------------------------------------------------------------------
'''

#input weight and height from user
weight = float(input("enter your weight(kg): "))
height = float(input("enter your height(m): "))

#calculate bmi
bmi = weight / (height * height)

#output bmi category
if bmi >= 25:
    print("You are overweight.")
elif bmi <= 18.5:
    print("You are underweight.")
else:
    print("Your weight is normal")