# Read the number of pins (N) and number of balls rolled (K)
N = int(input("Enter number of pins (N): "))
K = int(input("Enter number of balls (K): "))

# Initialize all N pins as standing ("I")
pins = ["I"] * N

print(f"\nEnter the {K} pairs of start and stop positions:")

# We will collect all incoming numbers into one big list
all_numbers = []
while len(all_numbers) < (K * 2):
    line = input()
    # This splits by any whitespace and filters out empty inputs
    all_numbers.extend(map(int, line.split()))

# Process the pairs from our list
for i in range(0, K * 2, 2):
    start = all_numbers[i]
    stop = all_numbers[i + 1]

    # Knock down the pins in the range (convert 1-index to 0-index)
    for j in range(start - 1, stop):
        pins[j] = "."

# Print the final result
print("\nRemaining pins:")
print("".join(pins))
