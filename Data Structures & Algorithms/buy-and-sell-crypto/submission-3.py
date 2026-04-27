class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding variable size window problem
        i , j = 0, 1
        profit = 0
        while j < len(prices):
            profit = max(profit, prices[j] - prices[i])

            if prices[j] < prices[i]:
                #window reset
                i = j
                j = i+1
            else:
                j += 1
        return profit



        