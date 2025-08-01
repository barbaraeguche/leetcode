# name: 701. insert into a binary search tree
# link: https://leetcode.com/problems/insert-into-a-binary-search-tree

# solution #
class Solution:
	def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
		if not root:
			return TreeNode(val)
		
		if val < root.val:
			root.left = self.insertIntoBST(root.left, val)
		else:
			root.right = self.insertIntoBST(root.right, val)
		
		return root
