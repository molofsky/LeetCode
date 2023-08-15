"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "*":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 * val1)
                case "/":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    div =  val2 // val1 + 1 if val2 * val1 < 0 and val2 % val1 != 0 else val2 // val1
                    stack.append(div)
                case "+":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 + val1)
                case "-":
                    val1 = stack.pop()
                    val2 = stack.pop()
                    stack.append(val2 - val1)
                case _:
                    stack.append(int(token))
                    
        return stack.pop()
