# name: 778. swim in rising water
# link: https://leetcode.com/problems/swim-in-rising-water

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
	
	def connected(self, n1, n2):
		return self.find(n1) == self.find(n2)

class Solution:
	def swimInWater(self, grid: List[List[int]]) -> int:
		n = len(grid)
		
		minHeap = []
		for i in range(n):
			for j in range(n):
				hq.heappush(minHeap, (grid[i][j], i, j))
		
		uf = UnionFind(n * n)
		directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
		
		while minHeap:
			t, r, c = hq.heappop(minHeap)
			
			for dr, dc in directions:
				nr, nc = dr + r, dc + c
				
				if (
					0 <= nr < n and
					0 <= nc < n and
					grid[nr][nc] <= t
				):
					uf.union(r * n + c, nr * n + nc)
			
			if uf.connected(0, n * n - 1):
				return t
		
		return -1

"""
time complexity:
- O(n^2 * log(n))

space complexity:
- O(n^2)
"""