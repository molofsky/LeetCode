"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and 
nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        result = []
        
        for i in range(n):
            if (i > 0 and nums[i - 1] == nums[i]):
                continue
                
            left, right = i + 1, n - 1
            
            while (left < right):
                total = nums[i] + nums[left] + nums[right]

                if (total == 0): 
                    result.append([nums[i], nums[left], nums[right]])

                    while (left < right and nums[left] == nums[left + 1]): left += 1 

                    while (left < right and nums[right] == nums[right - 1]): right -= 1
                        
                    left += 1
                    right -= 1

                elif (total < 0): 
                    left += 1
                else: 
                    right -= 1
        return result
