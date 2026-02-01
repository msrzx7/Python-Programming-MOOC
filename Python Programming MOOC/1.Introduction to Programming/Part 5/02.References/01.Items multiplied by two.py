# Write your solution here
def double_items(numbers: list):
    new_list=[] #creating seperate new list and adding values to it
    for item in numbers:
        new_list.append(item * 2)
    return new_list

if __name__ == "__main__":
    print(double_items(numbers)) 


### ANOTHER METHOD ###

def double_items(numbers: list):
    double = numbers[:] # creates new seperate duplicate list 
    for i in range(len(double)):
        double[i] *= 2
    
    return double