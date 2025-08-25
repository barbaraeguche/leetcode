# name: 787. cheapest flights within k stops
# link: https://leetcode.com/problems/cheapest-flights-within-k-stops

# solution #
class Solution:
	def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
		costs = [float("inf")] * n
		costs[src] = 0
		
		# bellman-ford algorithm
		for _ in range(k + 1):
			costCopy = costs[:]
			
			for u, v, c in flights:
				if costs[u] == float("inf"):
					continue
				if costs[u] + c < costCopy[v]:
					costCopy[v] = costs[u] + c
				
			costs = costCopy
		
		return -1 if costs[dst] == float("inf") else costs[dst]

"""
time complexity:
- O((n + m) * k); n is the number of vertices, m is the number of edges, k is the max number of stops

space complexity:
- O(n)
"""