"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many 
times as it shows in both arrays and you may return the result in any order.
"""

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num1 in nums1:
            if num1 in nums2:
                if num1 in res:
                    if (res.count(num1) < nums2.count(num1)): res.append(num1)
                else:
                    res.append(num1)
            
        return res
        
