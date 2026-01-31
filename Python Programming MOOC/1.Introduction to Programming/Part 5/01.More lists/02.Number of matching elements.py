# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for row in my_matrix:
        for number in row:
            if number == element:
                count += 1

    return count

def main():
    print(count_matching_elements(my_matrix, element))