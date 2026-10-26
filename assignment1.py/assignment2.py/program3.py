
day = int(input("Enter day="))
month = int(input("Enter month="))
year = int(input("Enter year="))

valid = True

if month < 1 or month > 12:
    valid= False
    print("Invalid month")
elif day < 1 or day > 31:
    valid = False
    print("Invalid day")


elif month == 4 or month == 6 or month == 9 or month == 11:
    if day > 30:
        valid = False
        print("Invalid day")


elif month == 2:
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("It's a Leap Year")

        if day > 29:
            valid = False
            print("Invalid day")

    else:
        
        if day > 28:
            valid = False
            print("Invalid day")

if valid:
    print("The date is valid.")
else:
    print("The date is invalid.")
