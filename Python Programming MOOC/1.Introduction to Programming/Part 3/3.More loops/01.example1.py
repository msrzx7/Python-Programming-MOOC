'''Please type in a number: 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
0
'''

n = int(input("Please type in number: "))
while n > 0:
    i = 0
    while i < n :
        print(i,end= ' ')
        i += 1
    n -=1
