"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def permuteHelper(nums, permuts):
            if not nums: 
                result.append(permuts)
            for i in range(len(nums)):
                permuteHelper(nums[:i] + nums[i + 1:], permuts + [nums[i]])
                
        permuteHelper(nums, [])
        return result
