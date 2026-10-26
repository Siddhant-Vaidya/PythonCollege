import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

dis = (b**2) - (4*a*c)

alpha = (-b - math.sqrt(dis)) / (2*a)
beta = (-b + math.sqrt(dis)) / (2*a)

print(f"The roots are = {alpha} and {beta}")
