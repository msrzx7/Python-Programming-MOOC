# Write your solution here
def longest(strings: list):
    string = ''
    for item in strings:
        if len(item) > len(string):
            string = item

    return string



if __name__ == "__main__":
    print(longest(strings))