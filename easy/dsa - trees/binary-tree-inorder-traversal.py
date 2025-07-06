# name: 94. binary tree inorder traversal
# link: https://leetcode.com/problems/binary-tree-inorder-traversal

# solution #
class Solution:
	def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		inorder = []
		
		def dfs(node: Optional[TreeNode]) -> None:
			if node:
				dfs(node.left)
				inorder.append(node.val)
				dfs(node.right)
		
		dfs(root)
		return inorder
	