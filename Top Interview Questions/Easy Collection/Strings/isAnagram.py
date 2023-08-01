"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters 
exactly once.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        count = {}
        
        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1
                
        
        for i in range(len(t)):
            if t[i] not in count:
                return False
            else:
                count[t[i]] -= 1
            if count[t[i]] < 0 : return False
            
        return True
