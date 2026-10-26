
a = int(input("Enter number of students in group A="))
b = int(input("Enter number of students in group B="))
c = int(input("Enter number of students in group C="))

desks_a = (a + 1) // 2
desks_b = (b + 1) // 2
desks_c = (c + 1) // 2

print("Total number of desks required=",desks_a + desks_b + desks_c)