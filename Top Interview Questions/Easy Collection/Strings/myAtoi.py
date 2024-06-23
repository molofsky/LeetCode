"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

1. Read in and ignore any leading whitespace.

2. Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This 
determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.

3. Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.

4. Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change 
the sign as necessary (from step 2).

5. If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 
Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.

6. Return the integer as the final result.

Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0: return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] == '-' or s[0] == '+': s = s[1:]
        res = 0
        
        for c in s:
            if c.isdigit():
                res = res * 10 + int(c)
            else:
                break
                
        res *= sign
        res = res if res >= -2**31 else -2**31
        res = res if res <= 2**31 - 1 else 2**31 - 1
        return res

        """
        Solution #2

        s2 = s.lstrip()
        if len(s2) < 1: return 0
        sign = 1
        i = 0
        if s2[0] == '-':
            sign *= -1
            i += 1
        if s2[0] == '+':
            i += 1
        
        while i < len(s2) and s2[i] == '0':
            i+=1
        
        res = []
        while i < len(s2):
            if not s2[i].isnumeric():
                break
            res.append(s2[i])
            i += 1
        
        if len(res) == 0: return 0
        res = sign * int("".join(res))
        if res > 2**31 - 1: res = 2**31 - 1
        if res < -2**31: res = -2**31
        return res
        """
