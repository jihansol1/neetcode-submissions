class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        # sort the candidates array 
        candidates.sort()

        def dfs(idx, currSum, currList):
            if currSum == target:
                res.append(currList.copy())
                return
            if idx >= len(candidates) or currSum > target:
                return 

            currList.append(candidates[idx])
            dfs(idx+1, currSum + candidates[idx], currList)

            currList.pop()

            # skip the idx if this idx was already seen to avoid duplicates
            while idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx += 1
            
            dfs(idx+1, currSum, currList)

        dfs(0,0,[])
        return res
