from typing import List

"""
Problem: Two Sum

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

Assumptions:
    - Each input has **exactly one solution**.
    - You may **not** use the same element twice.
    - The answer can be returned in **any order**.

Example 1:
Input:
    nums = [2, 7, 11, 15], target = 9
Output:
    [0, 1]
Explanation:
    - nums[0] + nums[1] = 2 + 7 = 9

Example 2:
Input:
    nums = [3, 2, 4], target = 6
Output:
    [1, 2]
Explanation:
    - nums[1] + nums[2] = 2 + 4 = 6

Example 3:
Input:
    nums = [3, 3], target = 6
Output:
    [0, 1]
Explanation:
    - nums[0] + nums[1] = 3 + 3 = 6

Constraints:
    - 2 <= len(nums) <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - There is **exactly** one solution.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}  # Dictionary to store seen numbers and their indices
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map:
                return [hash_map[complement], i]  # Return indices of complement and current number
            hash_map[num] = i  # Store number and its index
        return []  # Should never reach here since one solution is guaranteed

# Helper function to run tests
def run_test_case(nums, target, expected):
    result = sol.twoSum(nums, target)
    assert result == expected, f"Test failed for input {nums}, target {target}. Expected {expected}, got {result}"

# Initialize solution
sol = Solution()

# Test cases
run_test_case([2, 7, 11, 15], 9, [0, 1])
run_test_case([3, 2, 4], 6, [1, 2])
run_test_case([3, 3], 6, [0, 1])

print("All test cases passed!")
