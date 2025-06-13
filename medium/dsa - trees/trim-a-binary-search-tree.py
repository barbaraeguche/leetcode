# name: 669. trim a binary search tree
# link: https://leetcode.com/problems/trim-a-binary-search-tree

# solution #
class Solution:
	def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
		if not root:
			return root
		
		if root.val < low:
			return self.trimBST(root.right, low, high)
		elif root.val > high:
			return self.trimBST(root.left, low, high)
		
		# if within bounds
		root.left = self.trimBST(root.left, low, high)
		root.right = self.trimBST(root.right, low, high)
		
		return root

"""
time complexity:
- O(n)

space complexity:
- O(h); h is the height of the tree
"""