# Write your solution here

def line(n,str):
    if str == "":
        print('*'*n)
    else:
        print(str[0]*n)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")