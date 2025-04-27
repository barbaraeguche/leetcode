# name: 101. symmetric tree
# link: https://leetcode.com/problems/symmetric-tree

# solution #
class Solution:
	def isSymmetric(self, root: Optional[TreeNode]) -> bool:
		if not root: return True
		return self.mirror(root.left, root.right)
	
	@staticmethod
	def mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
		if left is None and right is None:
			return True
		elif left is None or right is None:
			return False
		
		return (
			left.val == right.val and
			Solution.mirror(left.left, right.right) and
			Solution.mirror(left.right, right.left)
		)
	