# Write your solution here
number = int(input("Please type in a number: "))
i = 1

while i <= number:
    if i == number:
        print(i)
        break
    print(i)
    print(number)
    
    i += 1
    number -= 1 