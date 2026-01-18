# Write your solution here
word  = input("Word: ")
print('*'*30)

if len(word) % 2 == 0: 

    space = (28 - len(word))//2
    print(f"*{' '*space}{word}{' '*space}*")
else:
    space1 = (28 - len(word))//2
    space2 = 28 - (len(word) + space1)
    print(f"*{' '*space1}{word}{' '*space2}*")
print('*'*30)