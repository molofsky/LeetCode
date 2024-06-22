"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        
        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1
                
        for i in range(len(s)):
            if count[s[i]] == 1:
                return i
        return -1

        """
        Solution # 2

        for i in range(len(s)):
            if s[i] not in s[:i] + s[i + 1:]:
                return i
        return -1
        """

        
