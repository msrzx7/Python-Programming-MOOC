# Write your solution here
def formatted(my_list: list):
    new_list = []
    for item in my_list:
        new_list.append(f"{item:.2f}")
        #:.2f tell how many "float" digits after deciaml
        print(new_list)
    return new_list

if __name__ == "__main__":
    print(formatted(my_list))

'''if  f"{name:15}" it means only 15 characters space is reserved'''