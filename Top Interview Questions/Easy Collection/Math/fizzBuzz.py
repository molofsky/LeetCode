"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [str(i) for i in range(1, n + 1)]
        
        for i in range(len(ans)):
            cur = int(ans[i])  
            if (cur % 3 == 0 and cur % 5 == 0): 
                ans[i] = "FizzBuzz"
            if (cur % 3 != 0 and cur % 5 == 0): 
                ans[i] = "Buzz"
            if (cur % 3 == 0 and cur % 5 != 0):
                ans[i] = "Fizz"

        return ans
