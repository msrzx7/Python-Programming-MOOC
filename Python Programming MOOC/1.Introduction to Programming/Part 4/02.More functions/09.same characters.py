# Write your solution here
def same_chars(str : str,a : int,b : int): # giving hint for each type of argument

    if a >= len(str) or b >= len(str):
        return False
    
    return str[a] == str[b] # checks the truthness

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))