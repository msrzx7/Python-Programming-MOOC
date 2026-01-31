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

def main():
    print(row_correct(sudoku,row_no))

main()



### another solution ###

def row_correct(sudoku: list, row_no: int):
    numbers = []
    for element in sudoku[row_no]:
        if element > 0 and element  in numbers:
            return False
            numbers.append(element)
        
    return True

