# Write your solution here
def spruce(height):

    print("a spruce!") # this row will always be printed
    row = "*"
    i = height

    while height > 0:
        print(" " * (height-1) + row)
        row += "**"
        height -= 1
    print(' '*(i-1)+ "*") # final will always be printed
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)


