# Task 6: Write a Python program that creates an empty list called `numbers`. 
# Prompt the user to enter five numbers and add them to the list. 
# Finally, print the sum of all the numbers in the list.

numbers = []
print("Enter 5 numbers: ")

for i in range(5):
    numbers.append(int(input()))

print("Sum of all numbers: ", sum(numbers))
