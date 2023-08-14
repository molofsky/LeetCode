"""
Given two integers a and b, return the sum of the two integers without using the operators + and -.
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        while (b != 0):
            carry = (a & b) & mask
            a = (a ^ b) & mask
            b = (carry << 1) & mask
        
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)
