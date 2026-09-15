class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low_buy = 0
        
        for i in range(1, len(prices)):
            if prices[low_buy] > prices[i]:
                low_buy = i
            else:
                max_profit = max(max_profit, prices[i] - prices[low_buy])

        return max_profit