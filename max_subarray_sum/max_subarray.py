def max_subarray_sum(arr, k):
    """
    Brute force approach to find the subarray with the maximum sum of size k.
    
    This approach considers all possible subarrays of size k and computes their sums 
    individually. It keeps track of the maximum sum and the corresponding subarray.

    Args:
        arr (list): List of integers.
        k (int): Size of the subarray.

    Returns:
        tuple: A tuple containing the maximum sum and the subarray with that sum.
    """
    n = len(arr)
    max_sum = 0
    max_subarray = []
    
    # Iterate through all possible subarrays of size k
    for i in range(n - k + 1):
        current_sum = sum(arr[i:i + k])
        if current_sum > max_sum:
            max_sum = current_sum
            max_subarray = arr[i:i + k]
    
    return max_sum, max_subarray


if __name__ == "__main__":
    # Example usage for Brute Force Approach
    max_sum, max_subarray = max_subarray_sum([2, 1, 5, 1, 3, 2], 3)
    print(f"Maximum sum: {max_sum}, Subarray: {max_subarray}")
    
    max_sum, max_subarray = max_subarray_sum([3, 2, 7, 5, 9, 6, 2], 3)
    print(f"Maximum sum: {max_sum}, Subarray: {max_subarray}")
