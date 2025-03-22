# name: 144. binary tree postorder traversal
# link: https://leetcode.com/problems/binary-tree-postorder-traversal

# solution #
class Solution:
	def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		postorder = []
		
		def traversal(node: Optional[TreeNode]) -> None:
			if node:
				traversal(node.left)
				traversal(node.right)
				postorder.append(node.val)
		
		traversal(root)
		return postorder
