# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")
while True:
    index = word.find(char)

    if index != -1 and index + 3 <=  len(word):# if the word is present and atleast 3 character long

        print(word[index:index + 3])  
        # printing 3 character from the index we got 
        word = word[index +1 : ]
        # move the word forward to search for the next occurrence

        break

# To approach this type of question requires a little bit of reasoning about indices and slicing. 
# Try pen paper for rough code and calculations etc.

### MODEL SOLUTION##
word = input("Please type in a word: ")
character = input("Please type in a character: ")

index = 0

while index + 3 <= len(word): # check the for 3 character long string 
    if word[index] == character:  # checking for each index which is equal to char
        print(word[index:index+3]) #  if it is then print 3 char. substring form that char
    index += 1  # updating index to go through each character to check for matcha