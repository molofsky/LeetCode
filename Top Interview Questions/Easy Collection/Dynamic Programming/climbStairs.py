"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        if (n == 1): return n
        
        ways = []
        ways.append(1)
        ways.append(1)
        for i in range(2, n + 1):
            ways.append(ways[i - 1] + ways[i - 2])
        return ways[-1]
