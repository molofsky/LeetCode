"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if (len(strs) == 0): return res
        if (len(strs) == 1): return strs[0]
        first_word = strs[0]
        count = 0
        break_flag = False
        
        for i in range(len(first_word)):
            for j in range(1, len(strs)):
                cur_word = strs[j]
                if i < len(cur_word) and cur_word[i] != first_word[i]:
                    break_flag = True
                    break
                if i >= len(cur_word): 
                    break_flag = True
                    break
                if j == len(strs) - 1: res += first_word[i]
            if (break_flag): break
        return res

        """
        Solution #2 

        if strs is None:
            return ""

        min_len = min(len(s) for s in strs)
        prefix = strs[0][:min_len]

        for i in range(min_len):
            for s in strs:
                if s[i] != prefix[i]:
                    return prefix[:i]
                    
        return prefix
        """
