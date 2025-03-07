"""
Problem Statement
Given three cups labeled "A", "B", and "C" with a ball initially placed in cup "B", determine the final position of the ball after performing a series of swaps. Each swap involves two cups, and the order of cups in the swap does not matter (e.g., "AB" is the same as "BA").

Examples:
Example 1:
Input: swaps = ["AB", "BC"]
Output: "A"
Explanation: 
- Initial position: B
- After swap "AB": ball moves to A
- After swap "BC": no change (ball remains in A)
- Final position: A

Example 2:
Input: swaps = ["BC", "AB"]
Output: "C"
Explanation: 
- Initial position: B
- After swap "BC": ball moves to C
- After swap "AB": no change (ball remains in C)
- Final position: C

Example 3:
Input: swaps = []
Output: "B"
Explanation: No swaps performed; ball remains in B.

Constraints:
- 1 <= len(swaps) <= 1000
- Each swap is a string of length 2 with distinct uppercase letters from "A", "B", "C".

Efficiency:
- Time Complexity: O(n) - Process each swap exactly once.
- Space Complexity: O(1) = Only track the current position of the ball.
"""

from typing import List

class Solution:
    def finalCupPosition(self, swaps: List[str]) -> str:
        ball_position = 'B'
        for swap in swaps:
            cup1, cup2 = swap[0], swap[1]
            if ball_position == cup1:
                ball_position = cup2
            elif ball_position == cup2:
                ball_position = cup1
        return ball_position

# Helper function to run tests
def run_test_case(swaps, expected):
    sol = Solution()
    result = sol.finalCupPosition(swaps)
    assert result == expected, f"Test failed for {swaps}. Expected {expected}, got {result}"

# Test cases
run_test_case(["AB", "BC"], "A")  # Example 1
run_test_case(["BC", "AB"], "C")  # Example 2
run_test_case([], "B")            # Example 3
run_test_case(["BA"], "A")        # Single swap (B to A)
run_test_case(["AC"], "B")        # Swap not involving B
run_test_case(["AB", "CA", "BC"], "B")  # Complex swaps

print("All test cases passed!")