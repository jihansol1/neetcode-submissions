class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(nums_arr):
            if not nums_arr:
                return 0
            if len(nums_arr) == 1:
                return nums_arr[0]
            n = len(nums_arr)
            dp = [0] * (n+1)
            dp[0] = 0
            dp[1] = nums_arr[0]

            for i in range(2, n+1):
                dp[i] = max(dp[i-1], dp[i-2] + nums_arr[i-1])

            return dp[n]

        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[0:len(nums)-1]), helper(nums[1:len(nums)]))

        

