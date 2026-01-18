# Write your solution here
vowel  = 'aeo'
string = input("Please enter a string: ")
index = 0
while index < len(vowel):
    if vowel[index] in string:
        print(vowel[index],"found")
    else:
        print(vowel[index],"not found")
    index += 1

# To check substring in string we use :
# substring in string 