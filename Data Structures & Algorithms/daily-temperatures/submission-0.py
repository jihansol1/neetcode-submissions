class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        results = len(temperatures) * [0]
        
        # pair (temp, index) in stack
        stack = []

        for i, t in enumerate(temperatures):
            # if stack is not empty and temp > top of stack
            while stack and t > stack[-1][0]:
                # update results array
                temp, ind = stack.pop()
                results[ind] = i - ind
            # append to stack
            stack.append([t, i])

        return results

