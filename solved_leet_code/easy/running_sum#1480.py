"""
https://leetcode.com/problems/running-sum-of-1d-array/description/

Problem Statement
Given an array `nums`, return the running sum of the array. The running sum is computed by adding all elements up to the current index sequentially.

Examples:
Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1]
Output: [1,2,3,4]
Explanation: Each element is the cumulative sum up to that index.

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:
- 1 <= nums.length <= 1000
- -10^6 <= nums[i] <= 10^6
"""

from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Compute running sum in-place
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

# Helper function to run tests
def run_test_case(nums, expected):
    result = sol.runningSum(nums)
    assert result == expected, f"Test failed for input {nums}. Expected {expected}, got {result}"

# Initialize solution
sol = Solution()

# Test cases
run_test_case([1,2,3,4], [1,3,6,10])       # Example 1
run_test_case([1,1,1,1], [1,2,3,4])         # Example 2
run_test_case([3,1,2,10,1], [3,4,6,16,17]) # Example 3
run_test_case([5], [5])                     # Single element
run_test_case([-1,2,-3,4], [-1,1,-2,2])     # Negative numbers
run_test_case([0,0,0], [0,0,0])             # All zeros

print("All test cases passed!")
