# name: 323. number of connected components in an undirected graph
# link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

# solution #
class UnionFind:
	def __init__(self, n):
		self.parent = {}
		self.rank = {}
		
		for i in range(0, n):
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
	def countComponents(self, n: int, edges: List[List[int]]) -> int:
		uf = UnionFind(n)
		components = n
		
		for src, dest in edges:
			if uf.union(src, dest):
				components -= 1
		
		return components

"""
time complexity:
- O(v + (e * α(v))); v is the number of vertices, e is the number of edges, α() is used for amortized complexity.

space complexity:
- O(v)
"""