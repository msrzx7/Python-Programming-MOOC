def dict_of_numbers():
    # special numbers and required number 
    units = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 
        15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"
    }
    
    tens = {
        2: "twenty", 3: "thirty", 4: "forty", 5: "fifty", 
        6: "sixty", 7: "seventy", 8: "eighty", 9: "ninety"
    }

    numbers = {}

    for i in range(100):
        if i < 20:
            numbers[i] = units[i]
        else:
            ten_digit = i // 10 # extracting tens digit
            one_digit = i % 10 # ones digit 
            
            if one_digit == 0: # if ones is 0
                numbers[i] = tens[ten_digit]
            else:
                numbers[i] = f"{tens[ten_digit]}-{units[one_digit]}" # combination of digits 
                
    return numbers

if __name__ == "__main__":

    numbers = dict_of_numbers()