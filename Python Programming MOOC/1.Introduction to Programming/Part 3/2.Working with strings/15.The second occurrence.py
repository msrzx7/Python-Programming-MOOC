# Write your solution here
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index = string.find(substring) # first occurance index

string2 = string[:index+len(substring)]
# slice of string till the first occurance of substring is found

if substring in string[len(string2):]:  # checkin for second occurance in remaing string 

    index2 = string[len(string2):].find(substring) # index of second occurance

    print(f"The second occurrence of the substring is at index {index2 + len(string2)}. ")
    # second occurance is whole string 
else:
    print("The substring does not occur twice in the string.")