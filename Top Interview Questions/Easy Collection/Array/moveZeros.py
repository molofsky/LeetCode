"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if (nums[i] != 0):
                nums[j], nums[i] = nums[i], nums[j]
                j+=1
        """
        Solution #2
        
        for i in range(len(nums)):
            if (nums[i] == 0):
                nums.remove(nums[i])
                nums += [0]
        Solution #3

        index_nonzero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index_nonzero] = nums[i]
                index_nonzero+=1
                
        for j in range(index_nonzero, len(nums)):
            nums[j] = 0
        """
