# Write your solution here
number = int(input("enter a number"))
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0 :
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")

#Note: 'and' always checks truthnes of both conditions if one them is false it will return false
# whereas 'or' return true if one of them is true.