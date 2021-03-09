#A school decided to replace the desk in three classroom. each desk sits two students .
#given the number of student in each class,print the smallest posible number of desks that can be purchased.
#the program should read three integers: the first number of the student in each of the three classes,a,band c respevctively.
#in the first test there are three group. the first group ha 20 student and thus need 10 desk.
#the second group has 21 students, so they can get by with no fewer than 11 desk.
#11 desk are also enough for the third group of 22 students. so, we need 32 desk in total.

class_a=int(input("enter the number of student that can in class A:\n"))
class_b=int(input("enter the number of student that can in class B:\n"))
class_c=int(input("enter the number of student that can in class C\n"))
desk_a=class_a//2
print(desk_a,"desk is nedded in class A")
desk_b=class_b//2
print(desk_b,"desk is nedded in class B")
desk_c=class_c//2
print(desk_c,"desk is nedded in class C")
remain_a=class_a%2
print(remain_a,"is the remaning desk")
remain_b=class_b%2
print(remain_b,"is the remaning desk")
remain_c=class_c%2
print(remain_c,"is the remainng desk")
total_desk=desk_a + desk_b + desk_c + remain_a + remain_b + remain_c
print(total_desk,"desk is nedded in total")
