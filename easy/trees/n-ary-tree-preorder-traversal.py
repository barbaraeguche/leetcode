# name: 589. n-ary tree preorder traversal
# link: https://leetcode.com/problems/n-ary-tree-preorder-traversal

# solution #
class Solution:
	def preorder(self, root: 'Node') -> List[int]:
		if not root:
			return []
		
		preorder = []
		stack = [root]
		
		while stack:
			node = stack.pop()
			preorder.append(node.val)
			
			for child in reversed(node.children):
				stack.append(child)
		
		return preorder
