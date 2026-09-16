class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # matrix dp[i][j] represents how many paths it took from top left to that cell
        # base case: all left and top border cells pre filled with their row # or col #
        
        dp = [[0] * (n+1) for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]

