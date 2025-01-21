# Maximum Subarray Sum Problem

This project demonstrates two approaches for solving the **Maximum Subarray Sum Problem** of a fixed size `k`:

1. **Brute Force Approach**: A straightforward method that iterates through all possible subarrays of size `k` and computes their sums.

2. **Sliding Window Approach**: An efficient approach that uses a sliding window to compute the maximum subarray sum in linear time.

## Problem Statement

Given an array `arr` and an integer `k`, the task is to find the subarray of size `k` with the maximum sum and return both the sum and the subarray.

---

## Approach 1: Brute Force

### Description
The brute force approach considers all possible subarrays of size k and computes their sums individually. It keeps track of the maximum sum and the corresponding subarray.

### Code

```python
def max_subarray_sum(arr, k):
    """
    Brute force approach to find the subarray with the maximum sum of size k.
    
    Args:
        arr (list): List of integers.
        k (int): Size of the subarray.
        
    Returns:
        tuple: Maximum sum and the subarray with that sum.
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
```

### Time Complexity:

* **Time Complexity:**  O(N * k), where `N` is the length of the array. For each subarray, we sum up `k` elements.
* **Space Complexity:** O(1), as we use only a constant amount of extra space.
---

## Approach 2: Sliding Window Approach

### Description:
The sliding window approach maintains a window of size `k` and slides it across the array. It calculates the sum of the initial window and updates the sum by subtracting the element that goes out of the window and adding the new element that comes into the window.

### Code:

```python
def max_subarray_sum_sliding_window(arr, k):
    """
    Sliding window approach to find the subarray with the maximum sum of size k.
    
    Args:
        arr (list): List of integers.
        k (int): Size of the subarray.
        
    Returns:
        tuple: Maximum sum and the subarray with that sum.
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
```

### Time Complexity:

* **Time Complexity:**  O(N), where `N` is the length of the array. We iterate through the array once.
* **Space Complexity:** O(1), as we use only a constant amount of extra space.
---

### Conclusion
* **Brute Force Approach:** Simple but inefficient for large arrays due to its quadratic time complexity.
* **Sliding Window Approach:** Efficient and ideal for large arrays since it computes the result in linear time.
---
