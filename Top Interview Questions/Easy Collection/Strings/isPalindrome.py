"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, 
it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s.lower() if c.isalnum())
        return s == s[::-1]
        
    """
    Solution #2

    s2 = s.lower().replace(' ', '')
        if len(s2) == 0: return True
        
        s_list = []
        for char in s2:
            if char.isalnum(): 
                s_list.append(char)
        
        return s_list[:] == s_list[::-1]
    """
