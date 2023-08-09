"""
Given an integer n, return the number of trailing zeroes in n!.
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact = math.factorial(n)
        count = 0
        while (fact % 10 == 0):
            count += 1
            fact //= 10
            
        return count
