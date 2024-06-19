"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        if (k > len(nums)): k = k % len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k] 
            
        """
        Solution 2

        k = k % len(num)
        nums[:] = nums[-k:] + nums[:-k]

        Solution 3
        
        n = len(nums)
        k = k % n
        
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
                
        nums.reverse()
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
        """
