# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")
index = word.find(char)
if index != -1 and index + 3 <=  len(word):
    print(word[index:index+3])


'''Note: string.find(substring/ character)tells the index of character or 
index from where substring is started. If the word is not present it will return "-1"'''

'''Mehtod: Methods are different from functions.
The difference is that methods are always attached to the object they are called on.
The object is the entity named before the method in the method call.
To find the substring we need to give arguement to the method.'''