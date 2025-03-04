"""
https://leetcode.com/problems/majority-element/

Problem Statement
Given an array `nums` of size `n`, return the majority element. The majority element is the element that appears more than ⌊n/2⌋ times. You may assume the majority element always exists in the array.

Examples:
Example 1:
Input: nums = [3,2,3]
Output: 3
Explanation: The element 3 appears 2 times (which is > ⌊3/2⌋ = 1).

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
Explanation: The element 2 appears 4 times (which is > ⌊7/2⌋ = 3).

Constraints:
- n == nums.length
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9
- The majority element always exists in the array.
"""

from typing import List

class Solution:
    # Using Boyer-Moore Voting Algorithm
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)
        return candidate

# Approach 2
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         return nums[n//2]


# Helper function to run tests
def run_test_case(nums, expected):
    result = sol.majorityElement(nums)
    assert result == expected, f"Test failed for input {nums}. Expected {expected}, got {result}"

# Initialize solution
sol = Solution()

# Test cases
run_test_case([3,2,3], 3)                # Example 1
run_test_case([2,2,1,1,1,2,2], 2)        # Example 2
run_test_case([5], 5)                     # Single element
run_test_case([1,1,2,2,2], 2)            # Majority in second half
run_test_case([-1, -1, -1], -1)          # Negative numbers
run_test_case([6,6,6,7,7,7,7,7,7], 7)    # Large majority

print("All test cases passed!")