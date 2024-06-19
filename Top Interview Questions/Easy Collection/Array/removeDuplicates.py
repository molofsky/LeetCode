"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears 
only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in 
nums initially. The remaining elements of nums are not important as well as the size of nums.

Return k.
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 1: return len(nums)
        
        cur_unique = nums[0]
        unique_idx = 1
        for i in range(1, len(nums)):
            num = nums[i]
            if (num != cur_unique):
                nums[unique_idx] = num
                cur_unique = num
                unique_idx += 1
        return unique_idx

        """
        Another Solution

        if not len(nums): return 0
        
        idx = 0
        for i in range(len(nums)):
            num = nums[i]
            if num not in nums[i + 1:]:
                nums[idx] = num
                idx += 1
                
        return idx
