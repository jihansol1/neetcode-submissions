class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # if total sum of nums is odd, can't have 2 equal subsets sum equal to it
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True # base case
        

        # dp[i] = True if can create subset to reach a target t

        for num in nums:
            for j in range(target, num-1, -1):
                if dp[j-num]:
                    dp[j] = True

        return dp[target]

