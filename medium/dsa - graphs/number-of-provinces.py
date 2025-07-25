# name: 547. number of provinces
# link: https://leetcode.com/problems/number-of-provinces

# solution #
class Solution:
	def findCircleNum(self, isConnected: List[List[int]]) -> int:
		size, adjacentList = len(isConnected), defaultdict(list)
		
		# build an adjacent list
		for i in range(size):
			for j in range(size):
				src, dest = isConnected[i][i], isConnected[i][j]
				
				# an undirected path
				if i != j and (src, dest) == (1, 1):
					adjacentList[i].append(j)
		
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
		
		for i in range(size):
			if not i in seen:
				dfs(i)
				components += 1
		
		return components

"""
time complexity:
- O(n^2)

space complexity:
- O(n)
"""