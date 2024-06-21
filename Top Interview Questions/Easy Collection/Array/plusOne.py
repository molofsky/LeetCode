"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] == 9: 
                digits[i] = 0 
            else: 
                digits[i] += 1
                return digits

        """
        digits.insert(0, 1) # insert returns None so we can't return immediately
        return digits
        """
        
        return [1] + digits

        """
        Solution #2

        temp = 0
        for i in reversed(range(len(digits))):
            temp = digits[i] + 1
            if temp < 10:
                digits[i] = temp
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
        return digits
        """
