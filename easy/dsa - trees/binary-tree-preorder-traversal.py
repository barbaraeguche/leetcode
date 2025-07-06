# name: 144. binary tree preorder traversal
# link: https://leetcode.com/problems/binary-tree-preorder-traversal

# solution #
class Solution:
	def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		preorder = []
		
		def dfs(node: Optional[TreeNode]) -> None:
			if node:
				preorder.append(node.val)
				dfs(node.left)
				dfs(node.right)
		
		dfs(root)
		return preorder
