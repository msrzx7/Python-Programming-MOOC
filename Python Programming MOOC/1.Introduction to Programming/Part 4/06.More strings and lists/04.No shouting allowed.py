# Write your solution here
def no_shouting(my_list: list):
    new_list =[]
    for word in my_list:
        if word.isupper():
            continue
        new_list.append(word)
    return new_list


if __name__ == "_main_":
    print(no_shouting(my_list))


### another method ###

def no_shouting(my_list: list):
    new_list = []
    for word in my_list:
        if not word.isupper(): # can use not which checks it's turthness and look for opposite mean islower()
            new_list.append(word)

    return new_list
