def range_sum(nums, i, j):
    """
    Calculate the sum of elements in the list 'nums' from index 'i' to 'j' (inclusive).
    
    Parameters:
    nums (list): A list of integers.
    i (int): The starting index (inclusive) of the range.
    j (int): The ending index (inclusive) of the range.
    
    Returns:
    int: The sum of the elements from index 'i' to 'j' in the list 'nums'.
    
    Example:
    >>> range_sum([1, 2, 3, 4, 5], 2, 3)
    7
    """
    return sum(nums[i:j+1])  # Sum between indices i and j (inclusive)


if __name__ == "__main__":
    # Example usage
    print(range_sum([1, 2, 3, 4, 5], 2, 3))  # Output: 7 (sum of elements between index 2 and 3: 3 + 4)
    print(range_sum([2, 4, 6, 8, 10], 1, 3)) # Output: 18 (sum of elements between index 1 and 3: 4 + 6 + 8)
    print(range_sum([2, 4, 6, 8, 10], 0, 4)) # Output: 30 (sum of elements between index 0 and 5: 2 + 4 + 6 + 8)
    
    