# Write your solution here
attempt = 0
while True:
    pin = input("PIN:")
    attempt += 1
    if pin == '4321' and attempt == 1:
        print("Correct! It only took you one single attempt!")
        break
    if pin == '4321':
        print(f"Correct! It took you {attempt} attempts")
        break
    print("Wrong")

#Note: Always check the initialisating and updating helper varialbes.