#write a python program to convert seconds to day,hour,minutes and second.
sec=int(input("enter the second you want to convert into day,hour minute"))
day=sec/(60*60*24)
hour=sec/(60*60)
minute=sec/(60)
print(f"the day is {day}")
print(f"the hour is {hour}")
print(f"the minute is {minute}