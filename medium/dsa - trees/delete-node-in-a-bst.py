# name: 450. delete node in a bst
# link: https://leetcode.com/problems/delete-node-in-a-bst

# solution #
class Solution:
	def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
		if not root:
			return root
		
		if key < root.val:
			root.left = self.deleteNode(root.left, key)
		elif key > root.val:
			root.right = self.deleteNode(root.right, key)
		else:
			# has only a right child
			if not root.left:
				return root.right
			# has only a left child
			if not root.right:
				return root.left
			
			# has both children
			node = self.getMinNode(root.right)
			# change the val
			root.val = node.val
			# remove min node
			root.right = self.deleteNode(root.right, node.val)
		
		return root
	
	def getMinNode(self, node: TreeNode) -> TreeNode:
		# custom classes are mutable
		temp = node
		
		while temp and temp.left:
			temp = temp.left
		return temp
