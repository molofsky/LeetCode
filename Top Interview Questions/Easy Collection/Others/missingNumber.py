"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the
array.
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arr = [False for i in range(len(nums) + 1)]
        
        for num in nums:
            arr[num] = True
        
        return arr.index(False)
