"""
https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/

Problem Statement
Given an array `nums`, for each element `nums[i]`, return the number of elements smaller than `nums[i]` to its right. 

Examples:
Example 1:
Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
- For nums[0]=8: There are four smaller numbers (1,2,2,3).
- For nums[1]=1: No smaller numbers exist.
- For nums[2]=2: One smaller number (1).
- For nums[3]=2: One smaller number (1).
- For nums[4]=3: Three smaller numbers (1,2,2).

Example 2:
Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Explanation: 
- For nums[0]=6: Two smaller numbers (5,4).
- For nums[1]=5: One smaller number (4).
- For nums[2]=4: No smaller numbers.
- For nums[3]=8: Three smaller numbers (6,5,4).

Example 3:
Input: nums = [7,7,7,7]
Output: [0,0,0,0]
Explanation: All elements are equal, so no smaller numbers.

Constraints:
- 2 <= nums.length <= 500
- 0 <= nums[i] <= 100
"""

from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # Sort the array to determine the count of smaller elements
        sorted_nums = sorted(nums)
        # Use a hash map to store the first occurrence index (count of smaller elements)
        hash_map = {}
        for i, num in enumerate(sorted_nums):
            if num not in hash_map:
                hash_map[num] = i
        # Build the result using the hash map
        result = []
        for num in nums:
            result.append(hash_map[num])
        return result

# Helper function to run tests
def run_test_case(input_nums, expected_output):
    result = sol.smallerNumbersThanCurrent(input_nums)
    assert result == expected_output, f"Test failed for input {input_nums}. Expected {expected_output}, got {result}"

# Initialize solution
sol = Solution()

# Test cases
run_test_case([8,1,2,2,3], [4,0,1,1,3])  # Example 1
run_test_case([6,5,4,8], [2,1,0,3])      # Example 2
run_test_case([7,7,7,7], [0,0,0,0])      # Example 3
run_test_case([5,0,10,0,10], [2,0,3,0,3])  # Duplicates and zeros
run_test_case([-1, -2, 0], [1,0,2])     # Negative numbers
run_test_case([1], [0])                  # Single element (edge case)

print("All test cases passed!")
