# Write your solution here
def list_sum(list1: list, list2: list):
    new_list = []
    for n in range(len(list1)):
        new_list.append(list1[n] + list2[n])
    return new_list

if __name__ == "__main__":
    print(list_sum(list1,list2))


### ANOTHER METHOD ###
def list_sum(list1: list, list2: list):
    new_list = []
    for item1 , item2 in zip(list1, list2): #creates new list by combining items in two or more lists
        new_list.append(item1 + item2)
    return new_list