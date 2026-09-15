class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, currSum, currList):
            if currSum == target:
                res.append(currList.copy())
                return
            if i >= len(nums) or currSum > target:
                return

            # option 1: include curr num
            currList.append(nums[i])
            dfs(i, currSum + nums[i], currList)

            # option 2: exclude curr num
            currList.pop()
            dfs(i+1, currSum, currList)

        dfs(0, 0, [])

        return res

        