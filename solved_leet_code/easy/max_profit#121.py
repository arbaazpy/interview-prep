"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Problem Statement
You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell it.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`.

Examples:
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

Example 2:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: No profitable transactions possible.

Constraints:
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

# Helper function to run tests
def run_test_case(prices, expected):
    sol = Solution()
    result = sol.maxProfit(prices)
    assert result == expected, f"Test failed for input {prices}. Expected {expected}, got {result}"

# Test cases
run_test_case([7,1,5,3,6,4], 5)
run_test_case([7,6,4,3,1], 0)
run_test_case([2,4,1], 2)  # Edge case: small array
run_test_case([3,2,6,5,0,3], 4)  # Multiple ups and downs
run_test_case([1,2], 1)  # Only one possible transaction

print("All test cases passed!")
