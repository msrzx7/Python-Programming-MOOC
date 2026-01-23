def line(n,str):
    if str == "":
        print('*'*n)
    else:
        print(str[0]*n)

def square_of_hashes(lenght):
    i = 0
    while i < lenght:
        line(lenght,'#')
        i += 1