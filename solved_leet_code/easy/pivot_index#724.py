"""
https://leetcode.com/problems/find-pivot-index/description/
https://leetcode.com/problems/find-the-middle-index-in-array/description/

Problem Statement
Given an integer array `nums`, return the **pivot index** of the array. The pivot index is the index where the sum of all numbers to the left of the index is equal to the sum of all numbers to the right of the index. If no such index exists, return `-1`.

Examples:
Example 1:
Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation: 
- Left sum = 1 + 7 + 3 = 11
- Right sum = 5 + 6 = 11
- Pivot at index 3.

Example 2:
Input: nums = [1,2,3]
Output: -1
Explanation: No index satisfies the condition.

Example 3:
Input: nums = [2,1,-1]
Output: 0
Explanation: 
- Left sum = 0 (no elements to the left)
- Right sum = 1 + (-1) = 0
- Pivot at index 0.

Constraints:
- 1 <= nums.length <= 10^4
- -1000 <= nums[i] <= 1000
"""

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == total - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1

# Helper function to run tests
def run_test_case(nums, expected):
    result = sol.pivotIndex(nums)
    assert result == expected, f"Test failed for input {nums}. Expected {expected}, got {result}"

# Initialize solution
sol = Solution()

# Test cases
run_test_case([1,7,3,6,5,6], 3)    # Example 1
run_test_case([1,2,3], -1)          # Example 2
run_test_case([2,1,-1], 0)          # Example 3
run_test_case([0], 0)               # Edge case: single element (sums to 0)
run_test_case([0,0,0,0], 0)         # All zeros, first index is pivot
run_test_case([-1,-1,-1,0,1,1], 0) # Pivot in middle with negative numbers

print("All test cases passed!")
