
name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000
print(f"my name is {name}, I am {age} years old")
print()
print("my skills are")
print(f" - {skill1} ({level1})\n - {skill2} ({level2})\n - {skill3} ({level3})")
print()
print(f"I am looking for a job with a salary of {str(lower)+'-'+str(upper)} euros per month")

''' Note: Always be extra careful while managing whitespaces.
Count them if necessary to make sure there are no more or less.
Try using f string and when ',' is added it adds extra space itself'''