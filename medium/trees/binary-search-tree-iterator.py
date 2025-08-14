# name: 173. binary search tree iterator
# link: https://leetcode.com/problems/binary-search-tree-iterator

# solution #
class BSTIterator:
	
	def __init__(self, root: Optional[TreeNode]):
		self.root = root
		self.stack = []
	
	def next(self) -> int:
		while self.hasNext():
			if self.root:
				self.stack.append(self.root)
				self.root = self.root.left
			else:
				self.root = self.stack.pop()
				break
		
		root, self.root = self.root, self.root.right
		return root.val
	
	def hasNext(self) -> bool:
		return self.root is not None or self.stack != []

"""
time complexity:
- O(1)

space complexity:
- O(h)
"""