class Solution:
    def maxProfit(self, prices: [int]) -> int:
        buyday = 0
        sellday = 1
        maxprofit = 0
        while sellday < len(prices):
            profit = prices[sellday] - prices[buyday]
            if profit > 0:
                maxprofit = max(profit, maxprofit)
            else:
                buyday = sellday
            sellday += 1

        return maxprofit

sol = Solution()

prices  = [7,1,5,3,6,4]
print(sol.maxProfit(prices))

prices  = [7,6,4,3,1]
print(sol.maxProfit(prices))