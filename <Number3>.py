total_sum = 0
for i in range(1, 6):
    number = float(input(f"Enter number {i}: "))
    total_sum += number
average = total_sum / 5

print("The sum of the numbers is:", total_sum)
print("The average of the numbers is:", average)