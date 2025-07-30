# name: 261. graph valid tree
# link: https://leetcode.com/problems/graph-valid-tree

# solution #
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
	def validTree(self, n: int, edges: List[List[int]]) -> bool:
		uf = UnionFind(n)
		components = 0
		
		for src, dest in edges:
			if uf.union(src, dest):  # the edge made a valid tree
				components += 1
			else:
				components -= 1  # edge caused a cycle
		
		return components == n - 1

"""
time complexity:
- O(m * α(n)); m is the number of edges, n is the number of nodes

space complexity:
- O(n)
"""