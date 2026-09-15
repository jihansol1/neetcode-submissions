class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t != "+" and t != "-" and t != "*" and t != "/":
                stack.append(int(t))
            else:
                second = stack.pop()
                first = stack.pop()

                if t == "+":
                    stack.append(first + second)
                elif t == "-":
                    stack.append(first - second)
                elif t == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(first / second))
        
        return stack[-1]