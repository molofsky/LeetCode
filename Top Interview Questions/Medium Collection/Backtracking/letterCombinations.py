"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the 
answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = []
        
        for i in range(len(digits)):
            match digits[i]:
                case "2":
                    letters.append(["a", "b", "c"])
                case "3":
                    letters.append(["d", "e", "f"])
                case "4":
                    letters.append(["g", "h", "i"])
                case "5":
                    letters.append(["j", "k", "l"])
                case "6":
                    letters.append(["m", "n", "o"])
                case "7":
                    letters.append(["p", "q", "r", "s"])
                case "8":
                    letters.append(["t", "u", "v"])
                case "9":
                    letters.append(["w", "x", "y", "z"])
        
        def combinationsHelper(idx, combs):
            if (idx == len(letters)):
                result.append(''.join(combs))
                return 
            
            for i in range(len(letters[idx])):
                combs[idx] = letters[idx][i]
                combinationsHelper(idx + 1, combs)
                                
        result = []
        if (len(letters) == 0): return result
        combs = [''] * len(letters)
        combinationsHelper(0, combs)
        return result
        
                    
