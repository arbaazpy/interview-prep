"""
https://leetcode.com/problems/fizz-buzz/description/

Problem Statement
Given an integer `n`, return a string array `result` (1-indexed) where:
- `result[i]` == "FizzBuzz" if `i` is divisible by both 3 and 5.
- `result[i]` == "Fizz" if `i` is divisible by 3.
- `result[i]` == "Buzz" if `i` is divisible by 5.
- `result[i]` == `i` (as a string) if none of the above conditions are true.

Examples:
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]
Explanation: 
- 1: "1"
- 2: "2"
- 3: "Fizz"

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Explanation: 
- 5 is divisible by 5 → "Buzz".

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
Explanation: 
- 15 is divisible by both 3 and 5 → "FizzBuzz".

Constraints:
- 1 <= n <= 10^4

Efficiency:
- Time Complexity: O(n) — Process each number exactly once.
- Space Complexity: O(n) — Store the result list of size n.
"""

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            output = ""
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            if not output:  # If no Fizz/Buzz, use the number itself
                output = str(i)
            result.append(output)
        return result

# Helper function to run tests
def run_test_case(input_n, expected):
    result = sol.fizzBuzz(input_n)
    assert result == expected, f"Test failed for n={input_n}. Expected {expected}, got {result}"

# Initialize solution
sol = Solution()

# Test cases
run_test_case(3, ["1","2","Fizz"])  # Example 1
run_test_case(5, ["1","2","Fizz","4","Buzz"])  # Example 2
run_test_case(15, ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"])  # Example 3
run_test_case(1, ["1"])  # Edge case: smallest input
run_test_case(2, ["1","2"])  # No Fizz/Buzz
run_test_case(6, ["1","2","Fizz","4","Buzz","Fizz"])  # Mix of Fizz and Buzz

print("All test cases passed!")