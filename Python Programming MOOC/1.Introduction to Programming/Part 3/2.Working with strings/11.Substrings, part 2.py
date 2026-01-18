# Write your solution here
string = input("Please type in a string: ")
index = len(string)

while index > 0:
    print(string[index-1:])
    index -= 1
