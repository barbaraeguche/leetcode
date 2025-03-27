# name: 104. maximum depth of binary tree
# link: https://leetcode.com/problems/maximum-depth-of-binary-tree

# solution #
class Solution:
	def maxDepth(self, root: Optional[TreeNode]) -> int:
		if root == None: return 0
		
		left = self.maxDepth(root.left)
		right = self.maxDepth(root.right)
		
		return max(left, right) + 1