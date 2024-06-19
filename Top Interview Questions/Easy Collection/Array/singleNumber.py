"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num # xor all elements in array leaves the unique number
        return res
        
        """
        Solution 2

        for i in range(len(nums)):
            num = nums[i]
            if num not in nums[:i] + nums[i + 1:]:
                return num
        
        return 0
        """
