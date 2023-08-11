"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            nums = [num for num in row if num != '.']
            if (len(nums) != len(set(nums))): return False
        
        for col in range(9):
            nums = [board[row][col] for row in range(9) if board[row][col] != '.']
            if (len(nums) != len(set(nums))): return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                nums = [board[row][col] for row in range(i, i + 3) for col in range(j, j + 3) if board[row][col] != '.']
                if (len(nums) != len(set(nums))): return False
        
        return True
