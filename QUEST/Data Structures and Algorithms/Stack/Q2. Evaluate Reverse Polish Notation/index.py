from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in "+-*/":
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:  # '/'
                    stack.append(int(a / b))  # truncates toward zero

        return stack[-1]


if __name__ == "__main__":
    solution = Solution()

    tokens1 = ["2", "1", "+", "3", "*"]
    tokens2 = ["4", "13", "5", "/", "+"]
    tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

    print("Output 1:", solution.evalRPN(tokens1))   # 9
    print("Output 2:", solution.evalRPN(tokens2))   # 6
    print("Output 3:", solution.evalRPN(tokens3))   # 22
