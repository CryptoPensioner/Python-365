# Task 9: Write a Python program that reads the content of a text file named "data.txt" and counts the number of lines in the file. 
# Print the count at the end.

file = open("data.txt", "r")
count = 0
for line in file:
    count += 1
print(count)
file.close()
