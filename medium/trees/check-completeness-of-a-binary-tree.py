# name: 958. check completeness of a binary tree
# link: https://leetcode.com/problems/check-completeness-of-a-binary-tree

# solution #
class Solution:
	def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
		queue = deque([root])
		prev = root
		
		while queue:
			node = queue.popleft()
			
			if node:
				# wasn't a node before this
				if not prev:
					return False
				
				queue.append(node.left)
				queue.append(node.right)
			
			# assign the last node to prev
			prev = node
		
		return True

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""