def find_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [10, 20, 30, 40, 50]
average = find_average(numbers)
print("The average of the numbers is:", average)
