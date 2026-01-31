# Write your solution here

def row_correct(sudoku: list, row_no: int):
    numbers = []
    for element in sudoku[row_no]:
        if element == 0:
            continue
        elif element not in numbers:
            numbers.append(element)
        else:
            return False

    return True

def column_correct(sudoku: list, column_no:int):
    numbers = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no]  in numbers:
            return False
        numbers.append(row[column_no]) 
            
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []

    for rows in sudoku[row_no: row_no + 3]:
        for element in rows[column_no:column_no + 3]:
            if element > 0 and element in numbers:
                return False
            numbers.append(element)
    
    return True

def sudoku_grid_correct(sudoku: list):
    row = [0,3,6]
    column = [0,3,6]
    
    for n in range(0,9):
        if row_correct(sudoku,n) == False:
            return False
    
        if column_correct(sudoku,n) == False:
            return False

    for i in row:
        for j in column:
            if block_correct(sudoku,i,j) == False:
                return False
    return True

 


