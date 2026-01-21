# Write your solution here
def squared(x,y):
    a = x * (y*y) # sizing string for potential slicing like problem 06
    b = y 
    while b > 0:
        print(a[:y]) # taking slice from start
        a = a[y:] # removing slce that's used
        b -= 1


### MODEL SOLUTION ###

def squared(characters, size):
    i = 0
    row = ""
    while i < size * size: # so it will to check and add each char. to row

        if i > 0 and i % size == 0: # To print the whole row at the end of line 
            print(row)
            row = ""
        row += characters[i % len(characters)] # adding char. till the line complete 
        # it checks char. to add by taking remaineder so we will knwo when the character will repeat 
        i += 1
    print(row) 
    # final line will be printed after the end of loop which cannot be otherwise because above
    # condition is not statisfied
