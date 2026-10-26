print("Enter the first timestamp (Hours, Minutes, Seconds):")
h1 = int(input("Hours 1: "))
m1 = int(input("Minutes 1: "))
s1 = int(input("Seconds 1: "))

print("\nEnter the second timestamp (Hours, Minutes, Seconds):")
h2 = int(input("Hours 2: "))
m2 = int(input("Minutes 2: "))
s2 = int(input("Seconds 2: "))


total_seconds1 = (h1 * 3600) + (m1 * 60) + s1
total_seconds2 = (h2 * 3600) + (m2 * 60) + s2

diff = total_seconds2 - total_seconds1

print("Difference=",diff)
