
max_streak = 0
current_streak = 0
prev_num = None

print("Enter numbers (end with 0):")

while True:
    num = int(input())

    if num == 0:
        
        break

    elif prev_num is None:
        
        current_streak = 1
        prev_num = num

    elif num == prev_num:
        
        current_streak = current_streak + 1

    else:
        
        if current_streak > max_streak:
            max_streak = current_streak
        
    
        current_streak = 1
        prev_num = num


if current_streak > max_streak:
    max_streak = current_streak

print("Widest fragment length:", max_streak)
