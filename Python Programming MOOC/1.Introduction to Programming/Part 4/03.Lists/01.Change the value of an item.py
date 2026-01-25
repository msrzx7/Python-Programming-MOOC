# Write your solution here
l = [1, 2, 3, 4, 5]
while True:
    index = int(input("Index: "))
    if index == -1 :
        break
    new_value = int(input("New Value: "))
    l[index] = new_value
    print(l)

### MODEL SOLUTION ###

list = [1, 2, 3, 4, 5]
while True:
    index = int(input("Index: "))
    if index == -1:
        break
    if index < 0 or index >= len(list): 
    # missing from code above checks that the input index should be in range.
    # However we don't need index < 0 as python support -ive indexing. It's for learning purpose.
        print("Index is outside of the range of the list")
        continue
    value = int(input("New value: "))
    list[index] = value
    print(list)