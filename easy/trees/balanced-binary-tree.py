# name: 110. balanced binary tree
# link: https://leetcode.com/problems/balanced-binary-tree

# solution #
class Solution:
	def isBalanced(self, root: Optional[TreeNode]) -> bool:
		def dfs(node: Optional[TreeNode]):
			if not node:
				return True, 0
			
			validLeft, leftHeight = dfs(node.left)
			validRight, rightHeight = dfs(node.right)
			
			# current height difference
			heightDiff = 1 + max(leftHeight, rightHeight)
			
			# check if balanced
			if abs(rightHeight - leftHeight) > 1:
				return False, heightDiff
			return validLeft and validRight, heightDiff
		
		return dfs(root)[0]
	
"""
time complexity:
- O(n)

space complexity:
- O(n)
"""