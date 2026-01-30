# Write your solution here
def most_common_character(string: str):
    count = 0
    letter = ''
    for char in string:
        if string.count(char) > count:
            count = string.count(char)
            letter = char
    return letter


if __name__ == "_main_":
    print(most_common_character(stringT))


### MODEL SOLUTION ###

def most_common_character(my_string: str):
    most_common = my_string[0] 
    for character in my_string:
        if my_string.count(character) > my_string.count(most_common):
        # checking count of each letter to the first letter and modfying it's value form the first letter to whoever is bigger than it 
            most_common = character

    return most_common