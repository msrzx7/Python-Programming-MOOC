# Write your solution here
def length_of_longest(my_list: list):
    word = ''
    for item in my_list:
        if len(word) < len(item):
            word = item
    return len(word)


def shortest(my_list):
    length = length_of_longest(my_list)
    result = ''
    for item in my_list:
        if length > len(item):
            length = len(item)
            result = item
    return result

if __name__ == "__main__":
    print(shortest(my_list))


### ANOTHER SOLUTION WITHOUT USING TWO FUNCIONS ###


def shortest(names: list):
    result = ""

    for nimi in names:
        if result == "" or len(nimi) < len(result):
            result = nimi

    return result