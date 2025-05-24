# name: 121. best time to buy and sell stock
# link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

# solution #
class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		price, profit = prices[0], 0
		
		for num in prices[1:]:
			# find min price as possible
			price = min(price, num)
			# find max profit as possible
			profit = max(profit, (num - price))
		
		return profit
