def create_prefix_sum(arr):
    """
    Calculate the prefix sum of the array 'arr'.
    
    The prefix sum array is constructed such that each element at index 'i' contains
    the sum of all elements from index 0 to 'i' in the original array.
    
    Parameters:
    arr (list): A list of integers to calculate the prefix sum for.
    
    Returns:
    list: The prefix sum array.
    
    Example:
    >>> create_prefix_sum([1, 2, 3, 4, 5])
    [1, 3, 6, 10, 15]
    """
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]  # Update the current element with the sum of itself and the previous element
    return arr


def range_sum(arr, i, j):
    """
    Calculate the sum of elements between indices 'i' and 'j' (inclusive) 
    using the prefix sum array.
    
    This function assumes that 'arr' is already the prefix sum array.
    
    Parameters:
    arr (list): A prefix sum array where each element at index 'i' contains the sum of elements from index 0 to 'i'.
    i (int): The starting index (inclusive) of the range.
    j (int): The ending index (inclusive) of the range.
    
    Returns:
    int: The sum of elements between indices 'i' and 'j' in the original array.
    
    Example:
    >>> range_sum([1, 3, 6, 10, 15], 2, 3)
    7
    """
    if i == 0:
        return arr[j]  # If the range starts from the beginning, return the value at index 'j'
    return arr[j] - arr[i-1]  # Otherwise, return the difference of the prefix sums


if __name__ == "__main__":
    # Example usage
    prefix_sum = create_prefix_sum([1, 2, 3, 4, 5])
    print(range_sum(prefix_sum, 2, 3))  # Output: 7 (sum of elements between index 2 and 3: 3 + 4)

    prefix_sum = create_prefix_sum([2, 4, 6, 8, 10])
    print(range_sum(prefix_sum, 1, 3))  # Output: 18 (sum of elements between index 1 and 3: 4 + 6 + 8)
    print(range_sum(prefix_sum, 0, 4))  # Output: 30 (sum of elements between index 0 and 5: 2 + 4 + 6 + 8)
