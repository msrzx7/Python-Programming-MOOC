# Write your solution here
student = int(input("How many students on the courses?"))
group = int(input("Desired group size?"))
group_formed = (student + group - 1)// group
print(f"Number of groups formed: {group_formed}")