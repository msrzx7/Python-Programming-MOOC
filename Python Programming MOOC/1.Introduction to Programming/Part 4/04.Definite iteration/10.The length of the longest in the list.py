# Write your solution here
def length_of_longest(my_list: list):
    word = ''
    for item in my_list:
        if len(word) < len(item):
            word = item
    return len(word)

if __name__ == "__main__":
    print(length_of_longest(my_list))
