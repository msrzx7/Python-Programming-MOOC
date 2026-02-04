# Write your solution here

def copy_matrix(matrix: list): # creates the copy of the matrix 
    new_matrix = []
    for row in matrix:
        new_matrix.append(row[:])
    return new_matrix

def transpose(matrix: list): # using the new copied matrix swapping the elements in original matrix
    new_matrix = copy_matrix(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = new_matrix[j][i]

''' The above code is not very optimized it's slow takes space to store the whole new matrix. To avoid repeation of same elements'''


if __name__ == "__main__":
    print(transpose(matrix))

### alternative method ###
''' Here we store the value in temp to avoid repeation of same element for tempoy period of time'''

def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j] # storing the value in temp
            matrix[i][j] = matrix[j][i] # swapping elements
            matrix[j][i] = temp # using temp to swap elements to avoid repeatation
 
            #..or alternatively, we could just swap like this without using temp
            # matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# Write your solution here