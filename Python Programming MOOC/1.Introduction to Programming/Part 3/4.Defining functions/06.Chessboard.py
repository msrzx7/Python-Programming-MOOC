def chessboard(n):
    b = 1
    a = '1010'* n

    while b <= n: 

        if b % 2 == 0: # checking for even row to start with 0
            print(a[1:n+1]) # slice will start from 0 to the size

        else:  # the odd row will start from 1
            print(a[:n]) # slice will start form 1 to the seze

        b +=1
        

####    MODEL SOLUTION #####

def chessboard(size):
    i = 0
    while i < size:
        if i % 2 == 0: # checks for even row
            row = "10"*size # sizing it for the potential need 
        else:
            row = "01"*size # for odd and sizing it 
            
        # Remove extra characters at the end of the row
        print(row[0:size])
        i += 1