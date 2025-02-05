"""
https://leetcode.com/problems/valid-palindrome/description/

Problem Statement
Given a string `s`, determine if it is a palindrome. A string is a palindrome if it reads the same forward and backward, ignoring non-alphanumeric characters and case differences.

Examples:
Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: True
Explanation: After removing non-alphanumeric characters and converting to lowercase: "amanaplanacanalpanama", which is a palindrome.

Example 2:
Input: s = "race a car"
Output: False
Explanation: After processing: "raceacar", which is not a palindrome.

Example 3:
Input: s = " "
Output: True
Explanation: An empty string is considered a palindrome.

Constraints:
- 1 <= s.length <= 2 * 10^5
- `s` consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Preprocess the string: keep alphanumeric characters and convert to lowercase
        processed = [char.lower() for char in s if char.isalnum()]
        
        # Check palindrome using two pointers
        left, right = 0, len(processed) - 1
        while left < right:
            if processed[left] != processed[right]:
                return False
            left += 1
            right -= 1
        return True

# Helper function to run tests
def run_test_case(input_str, expected):
    result = sol.isPalindrome(input_str)
    assert result == expected, f"Test failed for input '{input_str}'. Expected {expected}, got {result}"

# Initialize solution
sol = Solution()

# Test cases
run_test_case("A man, a plan, a canal: Panama", True)  # Example 1
run_test_case("race a car", False)                     # Example 2
run_test_case(" ", True)                               # Example 3 (edge case)
run_test_case("a", True)                               # Single character
run_test_case("abba", True)                            # Even-length palindrome
run_test_case("abcba", True)                           # Odd-length palindrome
run_test_case("0P", False)                             # Case sensitivity check
run_test_case("Able was I, ere I saw Elba", True)      # Complex case with punctuation

print("All test cases passed!")