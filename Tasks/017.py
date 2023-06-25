def divide_numbers(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Invalid input."
    
print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, 5))
print(divide_numbers(10, "a"))
