# name: 543. diameter of binary tree
# link: https://leetcode.com/problems/diameter-of-binary-tree

# solution #
class Solution:
	def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
		diameter = -1
		
		def dfs(node: Optional[TreeNode]):
			if not node:
				return 0
			
			nonlocal diameter
			
			leftHeight = dfs(node.left)
			rightHeight = dfs(node.right)
			
			# current height difference
			heightDiff = 1 + max(leftHeight, rightHeight)
			# current diameter
			diameter = max(diameter, leftHeight + rightHeight)
			
			return heightDiff
		
		dfs(root)
		return diameter
	
"""
time complexity:
- O(n)

space complexity:
- O(n)
"""