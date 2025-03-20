# name: 94. binary tree inorder traversal
# link: https://leetcode.com/problems/binary-tree-inorder-traversal

# solution #
class Solution:
	def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		inorder = []
		
		def traversal(node: Optional[TreeNode]) -> None:
			if node:
				traversal(node.left)
				inorder.append(node.val)
				traversal(node.right)
		
		traversal(root)
		return inorder