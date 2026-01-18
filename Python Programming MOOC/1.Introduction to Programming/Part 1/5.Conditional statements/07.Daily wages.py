# Write your solution here
hourly_wage = float(input("enter hourly wage"))
hours_worked = int(input("enter hours worked"))
day_of_the_week = input("enter day of the week")
if day_of_the_week != 'Sunday':
    print("Daily wages:",hourly_wage * hours_worked,"euros")
if day_of_the_week == 'Sunday':
    print("Daily wages:",2 * hourly_wage * hours_worked,"euros")
