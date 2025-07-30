# name: 133. clone graph
# link: https://leetcode.com/problems/clone-graph

# solution #
class Solution:
	def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
		graphMap = {}
		
		def dfs(root):
			# previously cloned
			if root in graphMap:
				return graphMap[root]
			
			# create a clone and store in map
			newNode = Node(root.val)
			graphMap[root] = newNode
			
			# clone its neighbors
			for neigh in root.neighbors:
				newNode.neighbors.append(dfs(neigh))
				
			return newNode
		
		return dfs(node) if node else None
	
"""
time complexity:
- O(v + e); v is the number of vertices, e is the number of edges

space complexity:
- O(v)
"""