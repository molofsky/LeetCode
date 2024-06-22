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

        """
        Solution #2

        for col_idx in range(9):
                col = []
                for row_idx in range(9):
                    cell = board[col_idx][row_idx]
                    if cell != '.':
                        col.append(cell)
                    if len(col) != len(set(col)):
                        return False
            
            for row_idx in range(9):
                row = []
                for col_idx in range(9):
                    cell = board[col_idx][row_idx]
                    if cell != '.':
                        row.append(cell)
                    if len(row) != len(set(row)):
                        return False
                    
            for col_idx in range(0, 9, 3):
                for row_idx in range(0, 9, 3):
                    sub_box = []
                    for col_idx2 in range(3):
                        for row_idx2 in range(3):
                            cell = board[col_idx + col_idx2][row_idx + row_idx2]
                            if cell != '.':
                                sub_box.append(cell)
                    if len(sub_box) != len(set(sub_box)):
                        return False
            
            return True
        """
