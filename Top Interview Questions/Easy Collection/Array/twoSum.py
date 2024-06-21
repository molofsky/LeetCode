"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j and nums[i] + nums[j] == target: 
                    res = [i, j] if i < j else [j, i]
                    break
        return res

        """
        Solution #2

        nums2 = [target - num for num in nums]
        j = 0
        
        for i in range(len(nums)):
                if nums[i] in nums2[:i] + nums2[i+1:]:
                    j = (nums2[:i] + nums2[i+1:]).index(nums[i])
                    if (j >= i): j = j + 1
                    if i > j:
                        return [j, i]
                    else:
                        return [i, j]
                
        return []
        """
