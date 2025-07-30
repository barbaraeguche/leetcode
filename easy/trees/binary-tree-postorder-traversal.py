# name: 145. binary tree postorder traversal
# link: https://leetcode.com/problems/binary-tree-postorder-traversal

# solution #
class Solution:
	def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		postorder = []
		
		def dfs(node: Optional[TreeNode]) -> None:
			if node:
				dfs(node.left)
				dfs(node.right)
				postorder.append(node.val)
		
		dfs(root)
		return postorder
