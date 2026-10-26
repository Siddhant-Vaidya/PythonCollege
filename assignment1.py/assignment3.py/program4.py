n=int(input("Enter no="))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1

if count==2:

    print(f"Your num is prime {n}")
else:
    print(f"Your num is not prime {n}")