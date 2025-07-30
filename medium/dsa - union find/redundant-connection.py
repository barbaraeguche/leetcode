# name: 684. redundant connection
# link: https://leetcode.com/problems/redundant-connection

# solution #
class UnionFind:
	def __init__(self, n):
		self.parent = {}
		self.rank = {}
		
		for i in range(1, n + 1):
			self.parent[i] = i
			self.rank[i] = 0
	
	def find(self, n):
		if n != self.parent[n]:
			self.parent[n] = self.find(self.parent[n])
		return self.parent[n]
	
	def union(self, n1, n2):
		p1, p2 = self.find(n1), self.find(n2)
		
		# already share a parent
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
	def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
		uf = UnionFind(len(edges))
		redundant = []
		
		for src, dest in edges:
			if not uf.union(src, dest):
				redundant = [src, dest]
		
		return redundant

"""
time complexity:
- O(v + (e * α(v))); v is the number of vertices, e is the number of edges, α() is used for amortized complexity.

space complexity:
- O(v)
"""