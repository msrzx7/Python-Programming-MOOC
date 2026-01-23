def line(n,str):
    if str == '':
        str = '*'
    print(str[0]*n)

def shape(triangle,x,rectangle,y):

    i = 1 
    while i <= triangle:
        line(i,x)
        i += 1

    while rectangle > 0:
        line(triangle,y)
        rectangle -= 1