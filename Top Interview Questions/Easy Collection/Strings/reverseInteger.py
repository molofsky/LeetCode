"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit
integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        x *= sign
        res = sign * int(str(x)[::-1])
        
        if res < -2**31 or res > 2**31 - 1: return 0
        return res
