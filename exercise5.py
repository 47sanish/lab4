#solve each of the following problems using python scripts
#make sure you use appropraite variable names and comments
#when there is a final answer have python print it to the screen
#a person's body mass index (BMI) is defined as; BMI=mass in kg\ (height in m)2


mass = float(input("enter the mass of person in kg;"))
height = float(input("enter th height of a person in meter"))
BMI = (mass/(height*height))
print(f"the BMI index of a person is {BMI}")
