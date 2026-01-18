# Write your solution here
n1 = int(input("enter number 1"))
n2 = int(input("enter number 2"))
operation = input("enter a operation")
if operation == 'add':
    print(f"{n1} + {n2} = {n1 + n2}")
if operation == 'subtract':
    print(f"{n1} - {n2} = {n1 - n2}")
if operation == 'multiply':
    print(f"{n1} * {n2} = {n1*n2}")