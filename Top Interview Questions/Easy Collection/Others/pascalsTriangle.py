"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            if (i == 0): 
                res.append([1])
            else: 
                prev_row = res[i - 1].copy()
                prev_row.insert(0, 0)
                prev_row.append(0)
                row = []
                for j in range(1, len(prev_row)):
                    row.append(prev_row[j - 1] + prev_row[j])
                res.append(row)
        
        return res
