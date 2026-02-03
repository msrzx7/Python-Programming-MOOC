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

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number # updating charcter


if __name__ == "__main__":
    print(print_sudoku(sudoku))
    print(add_number(sudoku,row_no,column_no,number))
    