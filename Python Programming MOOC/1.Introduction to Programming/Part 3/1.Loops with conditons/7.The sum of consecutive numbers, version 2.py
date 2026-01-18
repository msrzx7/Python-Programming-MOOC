# Write your solution here
limit = int(input("Limit: "))
current_sum = 0
n = 1
total = ""

while current_sum < limit:
    if current_sum == 0:
        total += f"{n}"
    else:
        total += f" + {n}"
    
    current_sum += n
    n += 1

print(f"The consecutive sum: {total} = {current_sum}")