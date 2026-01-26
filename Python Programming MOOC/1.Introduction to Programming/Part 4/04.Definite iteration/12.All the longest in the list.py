# Write your solution here
def all_the_longest(my_list: list):
    result = []
    word = ''
    for item in my_list:
        if len(word) < len(item):
            word = item
    result.append(word)

    for item in my_list:
        if len(word) == len(item) and word != item:
            word = item
            result.append(word)
    return result
if __name__ == "__main__":
    print(all_the_longest(my_list))


### MODEL SOLUTION ###

def all_the_longest(names: list):
    result = []

    for name in names:
        if result == [] or len(name) > len(result[0]): # if list is empty or we found new word longer than one before we change the list
            result = [name]
        elif len(name) == len(result[0]): # checks if any other word is equal to the length of longer word that we got
            result.append(name)

    return result