# name: 144. binary tree preorder traversal
# link: https://leetcode.com/problems/binary-tree-preorder-traversal

# solution #
class Solution:
	def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
		preorder = []
		
		def traversal(node: Optional[TreeNode]) -> None:
			if node:
				preorder.append(node.val)
				traversal(node.left)
				traversal(node.right)
		
		traversal(root)
		return preorder
