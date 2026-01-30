# Write your solution here
def no_vowels(string: str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        string = string.replace(vowel,'')
    return string


if __name__ == "_main_":
    print(no_vowels(string))


### MODEL SOLUTION ###
def no_vowels(my_string: str):
    vowels = "aeiou"
    result = ""

# checks for each letter that not in vowels and adding it to result to create new string.
    for letter in my_string:
        if letter not in vowels:
            result += letter

    return result
# Write your solution here