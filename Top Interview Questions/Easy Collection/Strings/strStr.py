"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not 
part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            res = haystack.index(needle)
        except ValueError:
            res = -1
        
        return res
