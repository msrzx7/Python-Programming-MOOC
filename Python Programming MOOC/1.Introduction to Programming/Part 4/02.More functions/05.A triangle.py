def line(n,str):
    if str == '':
        str = '*'
    print(str[0]*n)

def triangle(size):
    i = 1
    while i <= size:
        line(i,'#')
        i += 1