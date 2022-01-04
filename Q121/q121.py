from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_prices = [prices[0]]
        sell_prices = [prices[-1]]

        for i in range(1,len(prices)):
            buy_prices.append(min(buy_prices[-1], prices[i]))
        for i in range(len(prices)-2,-1,-1):
            sell_prices.append(max(sell_prices[-1], prices[i]))

        max_diff = 0
        for i,j in zip(buy_prices, sell_prices[::-1]):
            if j-i > max_diff:
                max_diff = j-i
        return max_diff

x = Solution()
print( x.maxProfit([7,1,5,3,6,4]) )