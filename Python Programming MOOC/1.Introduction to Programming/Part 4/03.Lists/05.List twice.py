# Write your solution here
my_list =[]
while True:
    new_item = int(input("New item: "))

    if new_item == 0:
        break

    my_list.append(new_item)
    print(f"The list now: {my_list}")
    
    sorted_list = sorted(my_list)
    print(f"The list in order: {sorted_list}")

print("Bye!")

''' sorted() sorts the list by making copy of list and sorting it. By conserving order of original list.
    whereas .sort() metod sorts the original list and changes it's order'''