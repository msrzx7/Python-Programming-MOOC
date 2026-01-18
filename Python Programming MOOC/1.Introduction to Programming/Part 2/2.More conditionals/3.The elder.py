# Write your solution here
name1 = input("Plese enter your name: ")
age1 = int(input("Please enter your age:"))
name2 = input("Please enter your name:")
age2 = int(input("Please enter your age"))
if age1 > age2:
    print("The elder is",name1)
elif age2 > age1:
    print("The elder is",name2)
else:
    print(f"{name1} and {name2} are the same age")
    