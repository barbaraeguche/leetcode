# name: 323. number of connected components in an undirected graph
# link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph

# solution #
class Solution:
	def countComponents(self, n: int, edges: List[List[int]]) -> int:
		adjacentList = defaultdict(list)
		
		# build an adjacent list
		for src, dest in edges:
			adjacentList[src].append(dest)
			adjacentList[dest].append(src)
		
		components, seen = 0, set()
		
		def dfs(src):
			# previously visited node
			if src in seen:
				return
			
			# mark node as seen
			seen.add(src)
			
			# explore connections
			for dest in adjacentList[src]:
				dfs(dest)
		
		for i in range(n):
			if not i in seen:
				dfs(i)
				components += 1
		
		return components

"""
time complexity:
- O(v + e)

space complexity:
- O(v + e)
"""