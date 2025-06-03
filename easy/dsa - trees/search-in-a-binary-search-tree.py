# name: 700. search in a binary search tree
# link: https://leetcode.com/problems/search-in-a-binary-search-tree

# solution #
class Solution:
	def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
		if not root:
			return None
		
		if root.val == val:
			return root
		
		if val < root.val:
			root = self.searchBST(root.left, val)
		else:
			root = self.searchBST(root.right, val)
		
		return root
	