class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        # use backtracking 
        # at each node, can add it or skip it
        def dfs(idx, currList, total):
            if total == target:
                output.append(currList.copy())
                return 
            if idx >= len(nums) or total > target:
                return

            # option 1: include curr num
            currList.append(nums[idx])
            dfs(idx, currList, total+nums[idx])
            currList.pop()
            # option 2: exclude curr num and skip it
            dfs(idx+1, currList, total)


        dfs(0, [], 0)
        return output
