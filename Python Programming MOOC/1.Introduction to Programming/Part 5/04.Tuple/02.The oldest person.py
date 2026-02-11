# Write your solution here
def oldest_person(people: list):
    oldest = 5000
    old_person = ''
    for person in people:
        if person[1] < oldest:
            oldest = person[1]
            old_person = person[0]

    return old_person
if __name__ == "__main__":
    print(oldest_person(people))


### another method ###

def oldest_person(people: list):
    oldest = people[0]
    for person in people:
        # comparing the year of birth of the oldest known person and the person in turn
        if person[1] < oldest[1]:
            oldest = person
 
    return oldest[0]
