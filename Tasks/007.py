def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

numbers = [1, 2, 3, 4, 5]
average = calculate_average(numbers)
print(average)

numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print(average)
