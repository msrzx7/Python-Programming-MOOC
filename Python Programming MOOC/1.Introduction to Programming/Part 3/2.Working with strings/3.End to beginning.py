# Write your solution here
string = input("Please type in a strng: ")
n = -1
while n >= -len(string):
    print(string[n])
    n -= 1

#Note: Indexing start from 0 and goes to len(string)-1 from first to last
# In last to first indexing start from -1 from last to -len(string) to first