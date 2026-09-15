class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # for n size nums, there should be 2^(n) sets of unique subsets

        output = []
        subset = []

        def dfs(idx):
            if idx >= len(nums):
                output.append(subset.copy())
                return 

            # Decision tree
            
            # 1. Add curr num
            subset.append(nums[idx])
            dfs(idx+1)

            # 2. Don't add curr num
            subset.pop()
            dfs(idx+1)

        dfs(0)

        return output

            


        """

        Use backtracking to solve:

        Go through num in nums
        At each num, have the choice to 
            1) Add num to subset
            2) Not add num to subset

            If subset is new, add to output array

        """

