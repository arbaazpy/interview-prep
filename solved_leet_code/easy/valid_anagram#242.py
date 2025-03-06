"""
https://leetcode.com/problems/valid-anagram/

Problem Statement
Given two strings `s` and `t`, determine if `t` is an anagram of `s`. An anagram is a word or phrase formed by rearranging the letters of another, using all the original letters exactly once.

Examples:
Example 1:
Input: s = "anagram", t = "nagaram"
Output: True
Explanation: Both strings contain the same letters with the same frequencies.

Example 2:
Input: s = "rat", t = "car"
Output: False
Explanation: 'r', 'a', 't' vs 'c', 'a', 'r' — different characters.

Example 3:
Input: s = "", t = ""
Output: True
Explanation: Empty strings are trivially anagrams.

Constraints:
- 0 <= len(s), len(t) <= 5 * 10^4
- `s` and `t` consist of lowercase English letters (or any valid Unicode characters, depending on problem constraints).
"""

from collections import defaultdict
from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Early exit if lengths differ
        if len(s) != len(t):
            return False
        
        # Count frequency of characters in s
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        # Decrement counts for characters in t
        for c in t:
            count[c] -= 1
            # If count goes negative, t has more of c than s
            if count[c] < 0:
                return False
        
        return True

    def isAnagram2(self, s: str, t: str) -> bool:
        # Early exit if lengths differ
        if len(s) != len(t):
            return False
        for c in set(s):
            if s.count(c) != t.count(c):
                return False
        return True

# Helper function to run tests
def run_test_case(s, t, expected):
    result = sol.isAnagram(s, t)
    assert result == expected, f"Test failed for s='{s}', t='{t}'. Expected {expected}, got {result}"

def run_test_case2(s, t, expected):
    result = sol.isAnagram2(s, t)
    assert result == expected, f"Test failed for s='{s}', t='{t}'. Expected {expected}, got {result}"


# Initialize solution
sol = Solution()

# Test cases
run_test_case("anagram", "nagaram", True)   # Example 1
run_test_case("rat", "car", False)          # Example 2
run_test_case("", "", True)                 # Example 3 (edge case)
run_test_case("a", "a", True)               # Single-character match
run_test_case("listen", "silent", True)     # Valid anagram
run_test_case("apple", "pale", False)       # Different lengths (5 vs 4)
run_test_case("aacc", "ccac", False)        # Same length but unequal counts

run_test_case2("anagram", "nagaram", True)   # Example 1
run_test_case2("rat", "car", False)          # Example 2
run_test_case2("", "", True)                 # Example 3 (edge case)
run_test_case2("a", "a", True)               # Single-character match
run_test_case2("listen", "silent", True)     # Valid anagram
run_test_case2("apple", "pale", False)       # Different lengths (5 vs 4)
run_test_case2("aacc", "ccac", False)        # Same length but unequal counts

print("All test cases passed!")