def max_subarray_sum(arr):
    current_max = arr[0]
    global_max = arr[0]

    for num in arr[1:]:
        current_max = max(num, current_max + num)
        if current_max > global_max:
            global_max = current_max

    return global_max

# Example usage
numbers = [-2, 3, -5, 7, -10]
print(max_subarray_sum(numbers))  # Output: 13
