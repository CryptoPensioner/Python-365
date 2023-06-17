# Task 8: Write a Python program that uses the `datetime` module to display the current date and time. 
# Import the necessary function(s) from the `datetime` module, retrieve the current date and time, and print it in a readable format.

import datetime

print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
