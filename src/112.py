# Chapter 2: Problem 1 - Finding a Missing Number
def find_missing_number(nums):
    n = len(nums)
    expected_sum = (n * (n + 1)) // 2  # Formula for finding the sum of first 'n' natural numbers

    total_sum = sum(nums)

    missing_number = expected_sum - total_sum
    return missing_number

# Example usage:
nums = [7, 3, 4, 9, 5]
missing_num = find_missing_number(nums)
print("The missing number is:", missing_num)
