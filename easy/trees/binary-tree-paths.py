# name: 257. binary tree paths
# link: https://leetcode.com/problems/binary-tree-paths

# solution #
class Solution:
	def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
		paths = []
		
		def validPaths(node: Optional[TreeNode], temp):
			if not node:
				return
			
			temp.append(str(node.val))
			
			# base case: path sum found and is at a leaf node
			if not (node.left or node.right):
				paths.append("->".join(temp[:]))
			else:
				# dfs till leaf node
				validPaths(node.left, temp)
				validPaths(node.right, temp)
			
			# backtrack from this node
			temp.pop()
		
		validPaths(root, [])
		return paths
	
"""
time complexity:
- O(n)

space complexity:
- O(n)
"""