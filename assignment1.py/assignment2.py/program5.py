# Take input from the user
s = input("Enter a string = ")
res= ""

for i in range(len(s)):

    if i % 3 != 0:
        res += s[i]

print("Final String =",res)

 