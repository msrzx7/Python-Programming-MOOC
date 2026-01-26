# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!


def palindromes(word: str):
    return word == word[::-1]

while True:
    word = input("Please type in palindrome: ")
    if palindromes(word):
        break
    else:
        print("that wasn't a palindrome")
print(f"{word} is a palindrome!")


## MODEL SOLUTION ##

def palindromes(word: str):
    for i in range(len(word)//2):
        if word[i] != word[len(word)-i-1]:
        # checking each character in word  through loops 
            return False
    return True

while True:
    word = input("Please type in a palindrome: ")
    if palindromes(word):
        print(word, "is a palindrome!")
        break
    print("that wasn't a palindrome")