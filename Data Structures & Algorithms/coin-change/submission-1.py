class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i-c]+1, dp[i])
        return dp[amount] if dp[amount] != float('inf') else -1