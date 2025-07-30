# name: 572. subtree of another tree
# link: https://leetcode.com/problems/subtree-of-another-tree

# solution #
class Solution:
	def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
		if not subRoot:
			return True
		if not root:
			return False
		
		if self.isSame(root, subRoot):
			return True
		
		return (
			self.isSubtree(root.left, subRoot) or
			self.isSubtree(root.right, subRoot)
		)
	
	def isSame(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
		if p is None and q is None:
			return True
		if p is None or q is None:
			return False
		
		return (
			p.val == q.val and
			self.isSame(p.left, q.left) and
			self.isSame(p.right, q.right)
		)
