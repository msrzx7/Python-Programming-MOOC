# Write your solution here
while True:
    editor = input("Editor: ").lower() # lower() method turns whole string to lower case


    if editor == 'word' or editor == 'notepad':
        print("awful")

    elif editor == 'visual studio code':
        print("an excellent choice!")
        break

    else:
        print("not good")
        
# .upper() mehtod turns whole string to upper case.