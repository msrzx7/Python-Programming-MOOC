# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []

    for rows in sudoku[row_no: row_no + 3]:
        for element in rows[column_no:column_no + 3]:
            if element > 0 and element in numbers:
                return False
            numbers.append(element)
    
    return True

def main():
    print(block_correct(sudoku,row_no,column_no))

main()