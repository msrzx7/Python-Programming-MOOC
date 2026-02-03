# Write your solution here
def print_sudoku(sudoku: list):
    for i in range(9):
        if i == 3 or i == 6: # blank line after line 3 and 6
            print()
        for j in range(9):
            element = sudoku[i][j]
            if element > 0: # printing number if it's not zero
                print(element,end='')
            else:
                print('_',end='') # replacing 0 with '_'

            if j < 8: # adding space between each character and last one should not have trailing space
                print(" ",end="")
            if j == 2 or j == 5: # adding extra space after 2nd and 5th character to create block 3 by 3 
                print(' ',end='')

        print() # to not add next print in same line


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    grid_copy = []
    for row in sudoku:
        grid_copy.append(row[:]) # adds a list completly to grid_copy list
        # we can't add like grid_copy = sudoku[:] as id doesn't work for nested list it references the same list as list inside list are all same

    grid_copy[row_no][column_no] = number

    return grid_copy

if __name__ == "__main__":
    print(copy_and_add(sudoku,row_no,column_no,number))

