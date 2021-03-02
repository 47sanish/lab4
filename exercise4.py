#given the integer N - the number of minute that is passed since midnight - how many  hours and minute are displayed
#on the 24h digital clock?
#the program should print two number; the number of hours (between 0 and 23)and the the number of minutes (between o and 59)
#for example, if n=150, 150 minute have passed since midnight - i.e.now

N=int(input("enter the minute passed since midnight:"))
hours=(N//60)
minute=(N%60)
print(f"the hours is {hours} ")
print(f"the minute is {minute}")
print(f"its {hours}:{minute} now")
