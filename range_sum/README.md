# Range Sum Problem

This project demonstrates two approaches for solving the **Range Sum Problem**:

1. **Brute Force Approach**: A straightforward method where the sum of elements is calculated by directly iterating over the range of indices.
2. **Prefix Sum Approach**: A more efficient method that computes the sum of elements in a given range in constant time, after preprocessing the array to calculate a prefix sum array.

## Problem Statement

Given an array `arr`, and multiple queries where each query specifies a range of indices `[i, j]`, the task is to calculate the sum of elements in the array from index `i` to `j` (inclusive).

---

## Approach 1: Brute Force

### Description:
The brute force approach directly iterates through the elements between indices `i` and `j` and computes their sum for each query.

### Code:

```python
def range_sum(nums, i, j):
    """
    Calculate the sum of elements in the list 'nums' from index 'i' to 'j' (inclusive).
    """
    return sum(nums[i:j+1])  # Sum between indices i and j (inclusive)
```

### Time Complexity:

* **Time Complexity:** O(N) per query, where `N` is the size of the range `[i, j]`. In the worst case, if all queries ask for the entire array, it will be O(N * Q), where `Q` is the number of queries.
* **Space Complexity:** O(1) as it uses only a constant amount of space.
---

## Approach 2: Prefix Sum

### Description:
The prefix sum approach preprocesses the array to create a prefix sum array, which allows answering range sum queries in constant time.

1. **Prefix Sum Array:** We compute an array where each element at index `k` contains the sum of all elements from the beginning of the array up to index `k-1`.
2. **Range Sum:** Using the prefix sum array, we can compute the sum of any subarray `[i, j]` by simply subtracting `prefix_sum[i-1]` from `prefix_sum[j]`.

### Code:

```python
def prefix_sum(arr):
    """
    Calculate the prefix sum of the array 'arr'.
    """
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]  # Update the current element with the sum of itself and the previous element
    return arr


def range_sum(arr, i, j):
    """
    Calculate the sum of elements between indices 'i' and 'j' (inclusive) using the prefix sum array.
    """
    if i == 0:
        return arr[j]  # If the range starts from the beginning, return the value at index 'j'
    return arr[j] - arr[i-1]  # Otherwise, return the difference of the prefix sums
```

### Time Complexity:

* **Preprocessing Time:** O(N), where `N` is the size of the array. We need to compute the prefix sum array.
* **Query Time:** O(1) for each range sum query, as we simply subtract two values from the prefix sum array.
* **Space Complexity:** O(N), since we store the prefix sum array.
---

### When to Use Which Approach

* **Brute Force:**
  * Use this approach when the range sum problem is small or when you only have a few queries to process.
  * It is simpler to implement but can be inefficient for large datasets or numerous queries.

* **Prefix Sum:**
  * The prefix sum approach is more efficient when you need to process multiple range sum queries.
  * It requires additional preprocessing time, but each query is answered in constant time, making it suitable for large arrays and many queries.
---

### Conclusion
* **Brute Force:** Simple but inefficient for large datasets with multiple queries.
* **Prefix Sum:** Efficient and ideal for large arrays with many queries, as it preprocesses the data in O(N) and answers each query in O(1).
---
