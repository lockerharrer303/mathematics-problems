def max_product_subarray(nums):
    """
    Find the contiguous subarray within an array (containing at least one number) 
    which has the largest product. This function implements Kadane's algorithm.
    
    Example usage:
    >>> max_product_subarray([-2, -3, 4])
    8
    """
    if not nums:  # If the input list is empty, return None
        return None
    
    max_product = current_max = nums[0]
    for num in nums[1:]:
        current_max = max(num, current_max * num)
        max_product = max(max_product, current_max)
    
    return max_product

# Example check function (not part of the code generation)
def check_solution():
    assert max_product_subarray([-2, -3, 4]) == 8
    assert max_product_subarray([1]) == 1
    assert max_product_subarray([-1, -2, -3, -4]) == -24
    print("All test cases passed.")

check_solution()
