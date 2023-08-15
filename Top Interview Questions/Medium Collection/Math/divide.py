"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, 
and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2**31, 2**31 
− 1]. For this problem, if the quotient is strictly greater than 2**31 - 1, then return 2**31 - 1, and if the quotient is strictly less than 
-2**31, then return -2**31.
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        if dividend == -2**31 and divisor == 1:
            return -2**31
        
        sign = (dividend < 0 and divisor >= 0) or (dividend >= 0 and divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
            
        quotient = 0
        while (dividend >= divisor):
            temp, mult = divisor, 1
            while (dividend >= (temp << 1)):
                temp <<= 1
                mult <<= 1
            
            dividend -= temp
            quotient += mult
        
        return -1 * quotient if sign else quotient
