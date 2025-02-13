"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

Problem Statement
Given an integer array `nums`, return `True` if any value appears at least twice in the array, and `False` if every element is distinct.

Examples:
Example 1:
Input: nums = [1,2,3,1]
Output: True
Explanation: The value 1 appears twice.

Example 2:
Input: nums = [1,2,3,4]
Output: False
Explanation: All elements are unique.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: True
Explanation: Multiple duplicates exist (1, 3, 4, 2).

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a set to track unique elements
        unique_nums = set(nums)
        # If lengths differ, duplicates exist
        return len(unique_nums) != len(nums)

# Helper function to run tests
def run_test_case(nums, expected):
    result = sol.containsDuplicate(nums)
    assert result == expected, f"Test failed for input {nums}. Expected {expected}, got {result}"

# Initialize solution
sol = Solution()

# Test cases
run_test_case([1,2,3,1], True)          # Example 1
run_test_case([1,2,3,4], False)          # Example 2
run_test_case([1,1,1,3,3,4,3,2,4,2], True)  # Example 3
run_test_case([], False)                 # Edge case: empty array (allowed by constraints?)
run_test_case([5], False)                # Single element
run_test_case([2,2,2,2], True)           # All elements duplicate
run_test_case([-1,2,-1], True)           # Negative numbers with duplicates

print("All test cases passed!")
