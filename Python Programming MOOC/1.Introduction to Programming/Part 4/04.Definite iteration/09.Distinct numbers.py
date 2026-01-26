# Write your solution here
def distinct_numbers(my_list: list):
    new_list = []
    for item in my_list:
        if item in new_list:
            continue
        new_list.append(item)
    return sorted(new_list)

if __name__ == "__main__    ":
    print(distinct_numbers(my_list))


### second method ###

def distinct_numbers(my_list: list):
    results = []
    for item in my_list:
        if item not in results: # not in checks the truthness of item not being in result
            results.append(item)

    results.sort()
    return results