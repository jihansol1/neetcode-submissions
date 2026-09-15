class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = [] # use stack to build valid parantheses

        def dfs(openPara, closedPara):
            if openPara == closedPara == n:
                res.append("".join(stack))
                return
            # open parantheses always must start before closed 
            if openPara < n:
                stack.append("(")
                dfs(openPara+1, closedPara)
                stack.pop() # undo to backtrack
            if closedPara < openPara:
                stack.append(")")
                dfs(openPara, closedPara+1)
                stack.pop() # undo to backtrack

        dfs(0,0)
        return res
