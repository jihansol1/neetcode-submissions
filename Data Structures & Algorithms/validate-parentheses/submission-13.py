class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = { ")":"(", "]":"[", "}":"{" }

        for i in range(len(s)):
            # if closed paranthesis
            if s[i] in m:
                if not stack or m[s[i]] != stack[-1]:
                    return False
                else:   
                    stack.pop()
            else:
                stack.append(s[i])

        return True if not stack else False