x1=int(input("Enter coordinate of x1="))
y1=int(input("Enter coordinate of y1="))
x2=int(input("Enter coordinate of x2="))
y2=int(input("Enter coordinate of y2="))
x3=int(input("Enter coordinate of x3="))
y3=int(input("Enter coordinate of y3="))

if x1 == x2:
        x4 = x3
elif x1 == x3:
        x4 = x2
else:
        x4 = x1

    
if y1 == y2:
        y4 = y3
elif y1 == y3:
        y4 = y2
else:
        y4 = y1

print("The fourth vertex is:")
print("x4=",x4)
print("y4=",y4)
