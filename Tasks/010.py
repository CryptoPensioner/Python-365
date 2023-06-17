# Task 10: Write a Python program that prompts the user to enter a number. 
# Use exception handling to handle the case where the user enters a non-numeric value. 
# If a non-numeric value is entered, display an error message. If a numeric value is entered, calculate and print its square.

input_number = input("Enter a number: ")
try:
    input_number = float(input_number)
    print(input_number ** 2)
except ValueError:
    print("Error: non-numeric value entered")
