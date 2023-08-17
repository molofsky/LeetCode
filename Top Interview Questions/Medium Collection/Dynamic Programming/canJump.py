"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your 
maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_max = 0
        
        for i in range(len(nums)):
            if i > jump_max: return False
            jump_max = max(jump_max, i + nums[i])
            
        return True
