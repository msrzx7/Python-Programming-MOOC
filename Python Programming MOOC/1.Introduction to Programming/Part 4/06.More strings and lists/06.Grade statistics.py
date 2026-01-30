# Write your solution here

my_list  = []
while True:
    score = input("Exam points and exercises completed: ")
    if score == '':
        break
    my_list += score.split()

a,b,c,d,e = 0,0,0,0,0
sum = 0
count = 0
fail = 0
new_list = []
for item in my_list:

    count += 1

    if count % 2 == 0:

        exercises = int(item)//10
        exam = int(my_list[count -2])
        points =(int(exercises) + int(exam))
        sum += points

        if exam < 10  or points <= 14 :
            fail += 1

        if points >= 28 and exam >= 10:
            a += 1

        elif points >= 24 and exam >= 10:
            b += 1

        elif points >=21 and exam >= 10:
            c += 1

        elif points >= 18 and exam >= 10:
            d += 1

        elif points >= 15 and exam >= 10:
            e += 1


print("Statistics:")
total = count/2
avg = print(f"Points average: {sum/(total):.1f}")

percentage = ((total-fail)/total)*100
print(f"Pass percentage: {percentage:.1f}")
print("Grade distribution:")
print(f"5: {'*'*a}")
print(f"4: {'*'*b}")
print(f"3: {'*'*c}")
print(f"2: {'*'*d}")
print(f"1: {'*'*e}")
print(f"0: {'*'*(fail)}")


### MODEL SOLUTON ###

def exam_and_exercise_completed(inpt):
# separating exercise completed and exam points and adding to list
    space = inpt.find(" ")
    exam = int(inpt[:space])
    exercise = int(inpt[space+1:])
    return [exam, exercise]

def exercise_points(amount):
# calculating exercise completed points 
    return amount // 10

def grade(points):
# instead of using a,b,c,d,e it uses much clearner version
    boundary = [0, 15, 18, 21, 24, 28]
    # list of minimum boundary for each group 
    for i in range(5, -1, -1):
    # range says strart with 5 go it 0 -1 not included and step is -1 which means go back 1 step
        if points >= boundary[i]:
        # If points are greater than or equal to the boundary,
        # return the corresponding grade
            return i

def mean(points):
    return sum(points) / len(points)

def main():
    points = []
    grades = [0] * 6 # List to count how many students got each grade (0–5)
    while True:
        inpt = input("Exam points and exercises completed: ")
        if len(inpt) == 0:
            break

        exam_and_exercises = exam_and_exercise_completed(inpt)
        exercise_pnts = exercise_points(exam_and_exercises[1])
        total_points = exam_and_exercises[0] + exercise_pnts

        points.append(total_points)
        grd = grade(total_points)
        if exam_and_exercises[0] < 10: # If exam points are less than 10 then the student is fail
            grd = 0
        grades[grd] += 1

    pass_pros = 100 * (len(points) - grades[0]) / len(points)

    print("Statistics:")
    print(f"Points average: {mean(points):.1f}")
    print(f"Pass percentage: {pass_pros:.1f}")
    print("Grade distribution:")
    
    for i in range(5, -1, -1):
    # Print grade distribution from highest to lowest grade
        stars = "*" * grades[i]
        print(f"  {i}: {stars}")

main()