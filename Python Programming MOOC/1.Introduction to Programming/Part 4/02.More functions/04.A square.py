def line(n,str):
    if str == '':
        str = '*'
    print(str[0]*n)

def square(size, character):
    i = 0
    while i < size:
        line(size,character)
        i += 1

square(5,'*')