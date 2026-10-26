
n = int(input("Enter numbers of cards="))
ExpectedSum = (n * (n + 1)) // 2

ActualSum = 0
for i in range(n - 1):
    card = int(input("Enter Card="))
    ActualSum += card

LostCard = ExpectedSum - ActualSum

print(f"Card which is lost is {LostCard}")
