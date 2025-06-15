# name: 938. range sum of bst
# link: https://leetcode.com/problems/range-sum-of-bst

# solution #
class Solution:
	def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
		def traversal(node):
			if not node:
				return 0
			
			# bst pruning
			if node.val < low:
				return traversal(node.right)
			if node.val > high:
				return traversal(node.left)
			
			return node.val + traversal(node.left) + traversal(node.right)
		
		return traversal(root)
