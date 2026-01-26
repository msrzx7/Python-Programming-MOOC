# Write your solution here
def anagrams(str1: str, str2: str):
    return sorted(str1) == sorted(str2)
'''sorted() turns both str1 and str2 in alphabetical order and by '== 'we are checking that there are same alphabet on same postion'''

if __name__ == "__main__":
    print(anagrams("tree","three"))