# name: 226. invert binary tree
# link: https://leetcode.com/problems/invert-binary-tree

# solution #
class Solution:
	def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		if not root: return None
		
		root.left, root.right = root.right, root.left
		
		self.invertTree(root.left)
		self.invertTree(root.right)
		
		return root
