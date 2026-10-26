no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))
no3 = int(input("Enter third number: "))

if (no1 >= no2) and (no1 >= no3):
    largest = no1
    print("The first number is largest =", largest)


elif (no2 >= no1) and (no2 >= no3):
    largest = no2
    print("The second number is largest =", largest)

else:
    largest = no3
    print("The third number is largest =", largest)

