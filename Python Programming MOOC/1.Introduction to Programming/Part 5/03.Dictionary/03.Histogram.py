    # Write your solution here
def histogram(string: str):
    group = {}
    for i in string:
        if i not in group:
            group[i] = 0
        group[i] += 1

    for keys,value in group.items():
        print(f"{keys} {'*'* value}")


if __name__ == "__main__":
    print(histogram(string))
    