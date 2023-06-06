# Task 4: Write a Python program that prompts the user to enter their age. If the age is greater than or equal to 18, print "You are eligible to vote." Otherwise, print "You are not eligible to vote."

age = input("How old are you? ")  # input() function was not covered by ChatGPT. I needed to Google "How to take input from a user in Python"

if int(age) >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
