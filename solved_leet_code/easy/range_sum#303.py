"""
https://leetcode.com/problems/range-sum-query-immutable/

Problem Statement
Design a class to handle multiple range sum queries on an integer array efficiently.

Implement the `NumArray` class:
1. `NumArray(nums: List[int])`: Initializes the object with the integer array `nums`.
2. `sumRange(left: int, right: int) -> int`: Returns the sum of elements from index `left` to `right` (inclusive).

Examples:
Example 1:
Input:
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output:
[null, 1, -1, -3]
Explanation:
- After initialization, sumRange(0, 2) → -2 + 0 + 3 = 1
- sumRange(2, 5) → 3 + (-5) + 2 + (-1) = -1
- sumRange(0, 5) → -2 + 0 + 3 + (-5) + 2 + (-1) = -3

Example 2:
Input:
["NumArray", "sumRange"]
[[[1, 2, 3, 4]], [0, 3]]
Output:
[null, 10]
Explanation: Sum of 1+2+3+4 = 10.

Constraints:
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- At most 10^4 calls will be made to `sumRange`.
"""

from typing import List

class NumArray:
    def __init__(self, nums: List[int]):
        # Build prefix sum array
        self.prefix = nums.copy()
        for i in range(1, len(self.prefix)):
            self.prefix[i] += self.prefix[i-1]

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]
        return self.prefix[right] - self.prefix[left - 1]

# Helper function to run tests
def run_test_case(operations, args, expected):
    obj = None
    results = []
    for op, arg in zip(operations, args):
        if op == "NumArray":
            obj = NumArray(arg[0])
            results.append(None)
        elif op == "sumRange":
            result = obj.sumRange(arg[0], arg[1])
            results.append(result)
    assert results == expected, f"Test failed. Expected {expected}, got {results}"

# Test cases
run_test_case(
    ["NumArray", "sumRange", "sumRange", "sumRange"],
    [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]],
    [None, 1, -1, -3]
)

run_test_case(
    ["NumArray", "sumRange"],
    [[[1, 2, 3, 4]], [0, 3]],
    [None, 10]
)

run_test_case(
    ["NumArray", "sumRange"],
    [[[5]], [0, 0]],
    [None, 5]  # Single element
)

run_test_case(
    ["NumArray", "sumRange", "sumRange"],
    [[[-1, 2, -3]], [0, 2], [1, 1]],
    [None, -2, 2]  # Negative numbers and single index
)

print("All test cases passed!")
