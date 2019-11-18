#get weight and height of user
weight = float(input("enter your weight(kg): "))
height = float(input("enter your height(m): "))

#calculate body mass index
bmi = weight / (height * height)

#determine what is overweight, underweight, and normal weight
if bmi >= 25:
    print("You are overweight.")
elif bmi <= 18.5:
    print("You are underweight.")
else:
    print("Your weight is normal")