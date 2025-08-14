# name: 1584. min cost to connect all points
# link: https://leetcode.com/problems/min-cost-to-connect-all-points

# solution #
import heapq as hq

class UnionFind:
	def __init__(self, n):
		self.parent = {}
		self.rank = {}
		
		for i in range(n):
			self.parent[i] = i
			self.rank[i] = 0
	
	def find(self, n):
		if n != self.parent[n]:
			self.parent[n] = self.find(self.parent[n])
		return self.parent[n]
	
	def union(self, n1, n2):
		p1, p2 = self.find(n1), self.find(n2)
		
		if p1 == p2:
			return False
		
		if self.rank[p1] < self.rank[p2]:
			self.parent[p1] = p2
		elif self.rank[p2] < self.rank[p1]:
			self.parent[p2] = p1
		else:
			self.parent[p1] = p2
			self.rank[p2] += 1
		
		return True

class Solution:
	def minCostConnectPoints(self, points: List[List[int]]) -> int:
		n = len(points)
		
		minheap = []
		for i in range(n):
			for j in range(i+1, n):
				xi, yi = points[i]
				xj, yj = points[j]
				
				d = abs(xi - xj) + abs(yi - yj)
				hq.heappush(minheap, (d, i, j))
		
		cost, uf = 0, UnionFind(n)
		
		while minheap:
			d, i, j = hq.heappop(minheap)
			
			if uf.union(i, j):
				cost += d
		
		return cost

"""
time complexity:
- O(n^2 * log(n))

space complexity:
- O(n^2)
"""