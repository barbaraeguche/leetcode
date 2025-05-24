# name: 98. validate binary search tree
# link: https://leetcode.com/problems/validate-binary-search-tree

# solution #
class Solution:
	def isValidBST(self, root: Optional[TreeNode]) -> bool:
		if not root:
			return True
		
		queue = deque([(root, float('-inf'), float('inf'))])
		
		while queue:
			node, left, right = queue.popleft()
			
			# not a valid bst
			if not (left < node.val < right):
				return False
			
			# recur for children nodes
			if node.left:
				queue.append([node.left, left, node.val])
			if node.right:
				queue.append([node.right, node.val, right])
		
		return True
