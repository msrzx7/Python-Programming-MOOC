# Write your solution here
l = []

while True:
    print("The list is now",l)
    action = input("a(d)d, (r)emove or e(x)it: ")
    if action == 'x':
        print("Bye!")
        break
    elif action == 'd':
        if l == []:
            l.append(1)
            continue
        l.append(l[-1] + 1)
    else:
        l.pop(-1)

### BETTER SOLUTION ###


my_list = []

while True:
    print(f"The list is now {my_list}")
    action = input("a(d)d, (r)emove or e(x)it: ")

    if action == 'x':
        break

    elif action == 'd':
        l.append(len(my_list) + 1)
    
    else:
        l.pop() # .pop() removes last index by default
print("Bye!")