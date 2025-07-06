# name: 938. range sum of bst
# link: https://leetcode.com/problems/range-sum-of-bst

# solution #
class Solution:
	def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
		def dfs(node):
			if not node:
				return 0
			
			# bst pruning
			if node.val < low:
				return dfs(node.right)
			if node.val > high:
				return dfs(node.left)
			
			return node.val + dfs(node.left) + dfs(node.right)
		
		return dfs(root)
