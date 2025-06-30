# name: 1791. find center of star graph
# link: https://leetcode.com/problems/find-center-of-star-graph

# solution #
class Solution:
	def findCenter(self, edges: List[List[int]]) -> int:
		degree = defaultdict(int)
		
		# use adjacent list
		for src, dest in edges:
			# undirected graph
			degree[src] += 1
			degree[dest] += 1
		
		# one of the source nodes has exactly n-1 destinations
		for src, count in degree.items():
			if count == len(edges):
				return src
		
		return -1

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""