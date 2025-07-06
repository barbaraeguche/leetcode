# name: 1971. find if path exists in graph
# link: https://leetcode.com/problems/find-if-path-exists-in-graph

# solution #
class Solution:
	def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
		adjacentList = defaultdict(list)
		
		# undirected graph
		for src, dest in edges:
			adjacentList[src].append(dest)
			adjacentList[dest].append(src)
		
		def dfs(src, dest, seen):
			# cannot be re-traversed
			if src in seen:
				return False
			# reached destination
			if src == dest:
				return True
			
			# add visited vertex to set
			seen.add(src)
			
			# dfs on its neighbours
			for neigh in adjacentList[src]:
				if dfs(neigh, dest, seen):
					return True
			
			return False
		
		return dfs(source, destination, set())

"""
time complexity:
- O(V + E)

space complexity:
- O(V + E)
"""