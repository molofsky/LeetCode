"""
Given an integer n, return the number of prime numbers that are strictly less than n.
"""

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        arr = [True for i in range(n)]
        
        for i in range(2, int(math.sqrt(n) + 1)):
            if (arr[i]):
                for j in range(i**2, n, i):
                    arr[j] = False
        return sum(arr) - 2
