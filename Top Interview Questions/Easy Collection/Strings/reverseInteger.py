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


        """
        Solution #2 
        
        sign = False
        if x < 0:
            sign = True
            x *= -1
        
        x_str = str(x)
        x_str2 = x_str[::-1] # strings are immutable, need new string x_str2, we cannot assing x_str[:] = x_str[::-1]
        
        res = -int(x_str2) if sign else int(x_str2)
        if res > 2**31 - 1 or res < -2**31: return 0
        return res
        ""
