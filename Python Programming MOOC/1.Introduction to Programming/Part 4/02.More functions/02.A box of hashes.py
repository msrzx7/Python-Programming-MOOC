# Copy here code of line function from previous exercise
def line(n,str):
    if str == "":
        print('*'*n)
    else:
        print(str[0]*n)

def box_of_hashes(height):
    while height - 1 > 0 :
        line(10,'#')
        height -= 1

    # You should call function line here with proper parameters
    # line(10, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)

'''Purpose of this exercise is to tell  that self made function can be called while defining other functions like print(), input(), etc.
    you can call a fuction after defining it first or it's a built-in fucntion.'''