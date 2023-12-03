Number10 = int(input('Enter Number 10'))
if (Number10 %3==0):
    print('Tic')
elif(Number10 %5==0):
    print('Tac')
elif(Number10 %3==0 and Number10 %5==0):
    print('Tic Tac')
else:
    print(Number10)
count=1
while count <= 20:
    print(count)
    count += 1
count = 1
while count <= 20:
    output = str(count) + ": "
    if count % 3 == 0 and count % 5 == 0:
        output += "Tic Tac"
    elif count % 3 == 0:
        output += "Tic"
    elif count % 5 == 0:
        output += "Tac"

    print(output)
    count += 1

import random
random_number = random.randint(1, 100)
print(f"Random Number: {random_number}")

attempts = 0
user_value = 0

while user_value <= 0 and attempts < 5:
    user_value = int(input("Enter a positive value: "))
    if user_value <= 0:
        print("Value must be greater than 0. Try again.")
        attempts += 1

if attempts == 5:
    print("Maximum attempts reached.")
else:
    print(f"You entered a positive value: {user_value}")