def find_sum_of_squares(nums):
    """
    Calculate the sum of squares of numbers in the list.

    Args:
    nums (list): A list of positive integers.

    Returns:
    int: The sum of squares of the numbers.
    """
    total = 0
    for num in nums:
        total += num ** 2
    return total

# Example usage:
nums = [1, 2, 3, 4]
print("The sum of squares is:", find_sum_of_squares(nums))
