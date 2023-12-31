"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II.
The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the 
number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number 
nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        cur = ""
        
        for i in reversed(range(len(s))):
            match s[i]:
                case 'M':
                    res += 1000
                    cur = 'M'
                case 'D':
                    res += 500
                    cur = 'D'
                case 'C':
                    if (cur == 'M' or cur == 'D'): res -= 100
                    else: res += 100
                    cur = 'C'     
                case 'L':
                    res += 50
                    cur = 'L'
                case 'X':
                    if (cur == 'L' or cur == 'C'): res -= 10
                    else: res += 10
                    cur = 'X'
                case 'V':
                    res += 5
                    cur = 'V'
                case 'I':
                    if (cur == 'V' or cur == 'X'): res -= 1
                    else: res += 1
                    cur = 'I'
        return res
        
            
