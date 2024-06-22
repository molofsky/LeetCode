"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix 
and do the rotation.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # Transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        # Reversing Rows
        for i in range(len(matrix)):
            matrix[i] = matrix[i][::-1]


"""
Side Problem: rotate the matrix counter-clockwise 
"""
class Solution:
    def rotate_counter(self, matrix: List[List[int]]) -> None:
        # Transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        # Reverse Columns
        for i in range(len(matrix));
            for j in range(len(matrix) // 2):
                matrix[j][i], matrix[len(matrix) - j - 1][i] = matrix[len(matrix) - j - 1][i], matrix[j][i]
