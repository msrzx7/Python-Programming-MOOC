# Write your solution here
limit = int(input("Upper limit: "))
sum = 0
n = 1
while sum < limit:
    sum += n
    n += 1
print(sum)