# Write your solution here
string = input("Please type in a string: ")
if len(string) > 1 and  string[1] == string[-2] :
    print(f"The second and the second to last characters are {string[1]}")
else:
    print("The second and the second to last characters are different")


# Note: string slicing or substring can be obtained by string[start_index : end_index]
# default start is 0 and end is -1 or len(string)
