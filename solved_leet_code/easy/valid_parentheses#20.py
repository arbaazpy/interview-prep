"""
https://leetcode.com/problems/valid-parentheses/description/

Problem Statement
Given a string `s` containing only the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Examples:
Example 1:
Input: s = "()"
Output: True

Example 2:
Input: s = "()[]{}"
Output: True

Example 3:
Input: s = "(]"
Output: False

Example 4:
Input: s = "([)]"
Output: False

Example 5:
Input: s = "{[]}"
Output: True

Constraints:
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        stack = []
        bracket_map = {")": "(", "]": "[", "}": "{"}
        
        for char in s:
            if char in bracket_map.values():  # Opening bracket
                stack.append(char)
            else:  # Closing bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
        
        return not stack  # True if stack is empty

# Helper function to run tests
def run_test_case(s, expected):
    result = sol.isValid(s)
    assert result == expected, f"Test failed for input '{s}'. Expected {expected}, got {result}"

# Initialize solution
sol = Solution()

# Test cases
run_test_case("()", True)
run_test_case("()[]{}", True)
run_test_case("(]", False)
run_test_case("([)]", False)
run_test_case("{[]}", True)
run_test_case("", True)          # Edge case: empty string
run_test_case("((()))", True)    # Nested parentheses
run_test_case("((())", False)    # Unclosed brackets
run_test_case("{[}]", False)     # Incorrect order

print("All test cases passed!")
