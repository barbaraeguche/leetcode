# name: 897. increasing order search tree
# link: https://leetcode.com/problems/increasing-order-search-tree

# solution #
class Solution:
	def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
		inorder = []
		
		# traverse the tree
		def dfs(node: Optional[TreeNode]) -> None:
			if not node:
				return
			
			dfs(node.left)
			inorder.append(node.val)
			dfs(node.right)
		
		dfs(root)
		
		root = TreeNode(inorder[0])
		node = root
		
		for val in inorder[1:]:
			node.right = TreeNode(val)
			node = node.right
		
		return root

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""