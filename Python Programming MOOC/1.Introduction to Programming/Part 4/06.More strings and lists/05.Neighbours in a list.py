# Write your solution here
def longest_series_of_neighbours(list: list):
    new_list = []
    length = 0
    for i in range(len(list)-1):
            if abs(list[i] -list[i + 1]) == 1:
                new_list.append(i)
            elif abs(list[i] - list[i + 1]) != 1:
                if length < len(new_list) : 
                    length = len(new_list)
                new_list = []
    if length < len(new_list) :
        length = len(new_list) 

    return length + 1


if __name__ == "_main_":
    print(longest_series_of_neighbours(list))


### MODEL SOLUTION ###


def longest_series_of_neighbours(my_list: list):
    longest = 1
    result = 1
    for i in range(1, len(my_list)):
        # function abs calculates the absolute value
        if abs(my_list[i-1]-my_list[i]) == 1:
            result += 1
            # don't have to use new_list as we can just result to keep track of connections and no plus 1 as it's started from 1 already
        else:
            result = 1
        # function max returns the highest of the parameters
        longest = max(longest, result)
    return longest