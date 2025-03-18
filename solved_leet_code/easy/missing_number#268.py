"""
https://leetcode.com/problems/missing-number/description/

Problem Statement
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

Examples:
Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: The numbers in [0,3] are [0,1,2,3]. 2 is missing.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: The numbers in [0,2] are [0,1,2]. 2 is missing.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: 8 is missing from the range [0,9].

Constraints:
- n == len(nums)
- 1 <= n <= 10^4
- 0 <= nums[i] <= n
- All numbers in `nums` are unique.

Efficiency
**Time Complexity**:  
- **O(n)** — We compute the sum of the array in a single pass.  
**Space Complexity**:  
- **O(1)** — No additional space is used beyond variables for the sum and length.  
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Sum of first (n+1) natural numbers (0 to n) minus sum of nums
        return n * (n + 1) // 2 - sum(nums)

# Helper function to run tests
def run_test_case(nums, expected):
    result = sol.missingNumber(nums)
    assert result == expected, f"Test failed for input {nums}. Expected {expected}, got {result}"

# Initialize solution
sol = Solution()

# Test cases
run_test_case([3,0,1], 2)               # Example 1
run_test_case([0,1], 2)                  # Example 2
run_test_case([9,6,4,2,3,5,7,0,1], 8)    # Example 3
run_test_case([0], 1)                    # Edge case: missing 1
run_test_case([1], 0)                    # Edge case: missing 0
run_test_case([1,2,3], 0)                # Missing first element
run_test_case([0,2,3], 1)                # Missing middle element

print("All test cases passed!")