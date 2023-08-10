"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        count = nums[0]
        
        for i in range(1, len(nums)):
            count = max(count + nums[i], nums[i])
            res = max(res, count)
        return res
