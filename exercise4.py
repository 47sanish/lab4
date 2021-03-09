#given the integer N - the number of minute that is passed since midnight - how many  hours and minute are displayed
#on the 24h digital clock?
#the program should print two number; the number of hours (between 0 and 23)and the the number of minutes (between o and 59)
#for example, if n=150, 150 minute have passed since midnight - i.e.now

#N=int(input("enter the minute passed since midnight:"))
#hours=(N//60)
#minute=(N%60)
#print(f"the hours is {hours} ")
#print(f"the minute is {minute}")
#print(f"its {hours}:{minute} now")

#solve each of the following problems using python scripts
#make sure you use appropraite variable names and comments
#when there is a final answer have python print it to the screen
#a person's body mass index (BMI) is defined as; BMI=mass in kg\ (height in m)2


mass = float(input("enter the mass of person in kg;"))
height = float(input("enter th height of a person in meter"))
BMI = (mass/(height*height))
print(f"the BMI index of a person is {BMI}")
