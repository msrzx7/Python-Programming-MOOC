# Write your solution here
letter = ''
letter1 = input("enter the letter: ")
letter2 = input("enter the letter: ")
letter3 = input("enter the letter: ")
if letter1 > letter2 and letter1 > letter3:
    if letter2 > letter3:
        letter = letter2
    else:
        letter = letter3
elif letter2 > letter1 and letter2 > letter3:
    if letter1 > letter3:
        letter = letter1
    else:
        letter = letter3
elif letter3 > letter1 and letter3 > letter2:
    if letter1 > letter2:
        letter = letter1
    else:
        letter = letter2
print("The letter in the middle is",letter)