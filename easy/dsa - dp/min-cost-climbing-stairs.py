# name: 746. min cost climbing stairs
# link: https://leetcode.com/problems/min-cost-climbing-stairs

# solution #
class Solution:
	def minCostClimbingStairs(self, cost: List[int]) -> int:
		for i in range(2, len(cost)):
			# min cost of the last two
			cost[i] += min(cost[i-2], cost[i-1])
		
		# min cost is going to be the last two
		return min(cost[-2], cost[-1])

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""