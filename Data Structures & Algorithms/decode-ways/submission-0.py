class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1 # base case to make dp logic valid

        for i in range(1, n+1):
            # if curr char is between 1-9
            if s[i-1] != "0":
                dp[i] += dp[i-1]

            # if curr char + prev element can form a valid code
            if i >= 2 and 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]

        return dp[n]
