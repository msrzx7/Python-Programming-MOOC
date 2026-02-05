# Write your solution here
phone_book = {}
while True:
    command = int(input("command (1 search, 2 add, 3 quit): "))
    if command == 3:
        print("quitting...")
        break
    name = input("name: ")
    if command == 2:
        number = input("number: ")
        phone_book[name] = number
        print("ok!")
    elif command == 3:
        if name in phone_book:
            print(phone_book[name])
        else:
            print("no number")

### model solution ###

''' instead of doing everything  in one loop and using if else block which can be complicated for readability, maintainability, and organization.
 we can make small funciton and use them in a loop for better readability, maintainability, and organization.'''

def search(persons):
    name = input("name: ")
    if name in persons:
        print(persons[name])
    else:
        print("no number")
 
def add(persons):
    name = input("name: ")
    number = input("number: ")
    persons[name] = number
    print("ok!")
 
def main():
    persons = {}
    while True:
        cmd = input("command (1 search, 2 add, 3 quit): ")
        if cmd == "1":
            search(persons)
        if cmd == "2":
            add(persons)
        if cmd == "3":
            break
    print("quitting...")
 
main()
# Write your solution here