# Write your solution here
cafeteria = int(input("How many times a week do you eat at the student cafeteria?"))
lunch = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))
print("Average food expenditure:")
print("Daily:",(cafeteria * lunch + groceries)/7,"euros")
print("Weekly:",cafeteria * lunch + groceries,"euros")

#Note: Always check datatype of input and output.