from typing import List

"""
Problem: Daily Temperatures

Given a list of daily temperatures `temperatures`, where each element `temperatures[i]` is the temperature in Fahrenheit for the day `i`,
your task is to return a list of integers `result` where `result[i]` represents the number of days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put `0` instead.

Example 1:
Input:
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
Output:
    [1, 1, 4, 2, 1, 1, 0, 0]

Explanation:
    - On day 0, the next warmer day is day 1 (temperature 74).
    - On day 1, the next warmer day is day 2 (temperature 75).
    - On day 2, the next warmer day is day 6 (temperature 76).
    - On day 3, the next warmer day is day 4 (temperature 72).
    - On day 4, the next warmer day is day 5 (temperature 72).
    - On day 5, the next warmer day is day 6 (temperature 76).
    - On day 6, there is no warmer day, so the result is 0.
    - On day 7, there is no warmer day, so the result is 0.

Example 2:
Input:
    temperatures = [30, 40, 50, 60]
Output:
    [1, 1, 1, 0]

Example 3:
Input:
    temperatures = [30, 60, 90]
Output:
    [1, 1, 0]

Constraints:
    - 1 <= len(temperatures) <= 10^5
    - 30 <= temperatures[i] <= 100

Note:
    - You should return a list of integers where each value corresponds to the number of days you have to wait for a warmer temperature, or `0` if there is no such day.
    - The solution should have an efficient time complexity, ideally O(n), where `n` is the number of days (length of the `temperatures` list).
"""

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            stack.append(i)
        return result

# Helper function to run tests
def run_test_case(temperatures, expected):
    result = sol.dailyTemperatures(temperatures)
    assert result == expected, f"Test failed for input {temperatures}. Expected {expected}, got {result}"

# Initialize solution
sol = Solution()

# Test cases
run_test_case([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0])
run_test_case([30, 40, 50, 60], [1, 1, 1, 0])
run_test_case([30, 60, 90], [1, 1, 0])

print("All test cases passed!")
