# Write your solution here
def invert(dictionary: dict):
    d = {}
    for keys, values in dictionary.items():
        d[values] = keys # adding keys and values swapped to new dict.
    dictionary.clear() # clearing original dict 
    dictionary.update(d) # adding keys and values to original dict, changing it's reference in global variable

if __name__ == "__main__":
    invert(dictionary)
    print(dictionary)


### another method ###

def invert(dictionary: dict):
	copy = {}
	for key in dictionary:
		copy[key] = dictionary[key] # creating copy of citionary
	for key in copy:
		del dictionary[key] # empty dictionary
	for key in copy:
		dictionary[copy[key]] = key # adding values to dictionary, dict[value of kyes in copy] = key in copy