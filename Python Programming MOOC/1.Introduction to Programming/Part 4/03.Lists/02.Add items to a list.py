# Write your solution here
n = int(input("How many itmes: "))
l = []
while len(l) < n:
    item = int(input(f"item {len(l) + 1}"))
    l.append(item)
print(l)    