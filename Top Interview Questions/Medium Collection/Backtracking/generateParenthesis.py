"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generateParenthesisHelper(s, left, right):
            if (len(s) == n * 2):
                pairs.append(s)
            if (left < n):
                generateParenthesisHelper(s + "(", left + 1, right)
            if (right < left):
                generateParenthesisHelper(s + ")", left, right + 1)
        
        pairs = []
        generateParenthesisHelper("", 0, 0)
        return pairs
