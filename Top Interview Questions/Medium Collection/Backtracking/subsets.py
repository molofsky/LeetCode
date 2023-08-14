"""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.
"""

class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
      result = []
      
      def subsetHelper(index, subset):
          result.append(subset[:])
          for i in range(index + 1, len(nums)):
              subset.append(nums[i])
              subsetHelper(i, subset)
              subset.pop()
      
      subsetHelper(-1, [])
      return result
            
      """ 
      Solution w/o Backtracking
      result = [[]]
      for num in nums:
          result += [cur + [num] for cur in result]
      return result
      """
        
            
