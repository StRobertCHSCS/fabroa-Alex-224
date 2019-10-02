# get number of students and number of chicken from user
students = int(input("number of students: "))
fried_chicken = int(input("number of fried chickens: "))

# calculate number of chicken divided and left over
chicken_for_students = int(int(fried_chicken)/int(students))
chicken_for_fabroa = fried_chicken % students

# output number of chicken each student gets and how much Mr. Fabroa gets
print("the students each get " + str(chicken_for_students), end="")
print(" and Mr.Fabroa gets " + str(chicken_for_fabroa))