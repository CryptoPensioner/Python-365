# Task 5: Write a Python program that prompts the user to enter a positive integer and prints all the numbers from 1 to that integer using a `for` loop.


num = int(input("Enter a positive integer: "))
i = 1

print("Using a `for` loop:")
# It can be done using range() function, but it wasn't covered by ChatGPT
for i in range(1, num + 1):
    print(i)

print("Using a `while` loop:")
i = 1
# Or using a `while` loop, but our task was to use a `for` loop
while i < num + 1:
    print(i)
    i += 1

print("Using a `for` loop and a list:")
i = 1
# I would never come up with that myself, but I found this solution, using list. In theory it doesn't use any functions CHatGPT didn't cover yet, but lists and arrays ware not covered eather...
for _ in [None] * num:
    print(i)
    i += 1
