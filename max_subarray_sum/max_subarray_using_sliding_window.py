def max_subarray_sum_sliding_window(arr, k):
    """
    Sliding window approach to find the subarray with the maximum sum of size k.
    
    This approach maintains a window of size k and slides it across the array.
    It starts by calculating the sum of the initial window, then iteratively updates 
    the sum by subtracting the element that goes out of the window and adding the 
    element that comes into the window.

    Args:
        arr (list): List of integers.
        k (int): Size of the subarray.

    Returns:
        tuple: A tuple containing the maximum sum and the subarray with that sum.
    """
    n = len(arr)
    current_sum = sum(arr[:k])  # Initial sum of the first window
    max_sum = current_sum
    max_start_index = 0
    
    # Iterate through the array, sliding the window
    for i in range(n - k):
        current_sum = current_sum - arr[i] + arr[i + k]
        if current_sum > max_sum:
            max_sum = current_sum
            max_start_index = i + 1
    
    return max_sum, arr[max_start_index:max_start_index + k]


if __name__ == "__main__":
     # Example usage for Sliding Window Approach
    max_sum, max_subarray = max_subarray_sum_sliding_window([2, 1, 5, 1, 3, 2], 3)
    print(f"Maximum sum: {max_sum}, Subarray: {max_subarray}")
    
    max_sum, max_subarray = max_subarray_sum_sliding_window([3, 2, 7, 5, 9, 6, 2], 3)
    print(f"Maximum sum: {max_sum}, Subarray: {max_subarray}")
