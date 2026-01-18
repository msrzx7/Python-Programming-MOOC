# Write your solution here
sentence = ''
char =''
while True:
    word = input("Please type in a word: ")
    if (word == 'end') or char == word:
        break
    char = word
    sentence += word + ' '
print(sentence)

#Note: Made a mistake by mistooking word comming twice 
# and word coming twice in a row