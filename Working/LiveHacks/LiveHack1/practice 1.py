'''
-------------------------------------------------------------------------------
Name:		practice.py
Purpose:	calculate celsius from farenheit

Author:	Yu.A

Created:	october 1 2019
------------------------------------------------------------------------------
'''

# get farenheit from user
farenheit = float(input("enter the farenheit: "))

# compute celsius from farenheit
celsius = (5/9)*(farenheit - 32)

# output celsius
print("the temperature in celsius is " + str(celsius))