# name: 2144. minimum cost of buying candies with discount
# link: https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount

# solution #
class Solution:
	def minimumCost(self, cost: List[int]) -> int:
		# sort in descending order
		cost.sort(reverse=True)
		
		# group by three each
		# you buy the first two and take the third free
		cost = [cost[i:i+3] for i in range(0, len(cost), 3)]
		
		money = 0
		
		for c in cost:
			money += sum(c[:2])
		
		return money
	