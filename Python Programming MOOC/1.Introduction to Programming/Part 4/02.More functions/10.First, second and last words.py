# Write your solution here
def first_word(line : str):
    word = ''
    i = 0
    while i < len(line):

        if line[i] == ' ':
            return word
        
        word += line[i]
        i += 1
        


def second_word(line: str):
    i = 0
    space = 0
    word = ''
    while i < len(line):
        if line[i] == ' ':
            space += 1
        if space == 1 and line[i] != ' ':
            word += line[i]
        i += 1
    return word

def last_word(line: str):
    word = ''
    i = -1 
    while i < len(line):
        if line[i] != ' ':
            word += line[i] # adding letter from last to first in last word
        if line[i] == ' ':
            return word[::-1] # reversing the final return 
        i -= 1



# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))

### MODEL SOLUTION ###

''' A single function is defined here instead of writing logic for all three over and over.
It calculates for any given word.'''
def find_word(str, whatth):
    index = 0
    word = ""
    counter = 0
    while index < len(str):
    	if str[index] == " ":
    	    counter += 1
    	    if counter == whatth: # encountring 1st space mean 1st word is complete so on for other so checking space no. and word no.
    	        break
    	    word = ""
    	else:
    	    word += str[index]
    	index += 1
    return word

def first_word(mjono):
    return find_word(mjono, 1)

def second_word(mjono):
    return find_word(mjono, 2)

def last_word(mjono):
    return find_word(mjono, 0) 

''' In last_word() it will not break immediately because first space conditon is not satisfied and when it does index is move ahead.
So it will run for the whole line until while condition is satisfied clearing word after each space encounter and only the last word is 
stored. '''
# Write your solution here
