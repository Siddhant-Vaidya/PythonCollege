
h = int(input("Enter Hours (0-11): "))
m = int(input("Enter Minutes (0-59): "))
s = int(input("Enter Seconds (0-59): "))

if (0 <= h < 12) and (0 <= m < 60) and (0 <= s < 60):
        angle = (h * 30) + (m * 0.5) + (s * (1/120))
        print(f"The angle of the hour hand is: {angle} degrees")

else:
        print("Invalid input! Please enter times within the allowed ranges.")
