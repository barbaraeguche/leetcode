# name: 617. merge two binary trees
# link: https://leetcode.com/problems/merge-two-binary-trees

# solution #
class Solution:
	def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
		# edge cases
		if not root1:
			return root2
		if not root2:
			return root1
		
		# use bfs to alter root1 nodes
		queue = deque([(root1, root2)])
		
		while queue:
			n1, n2 = queue.popleft()
			
			# change root1 node val
			n1.val += n2.val if n2 else 0
			
			# since we alter root1, if there is no root2, continue
			if not n2:
				continue
			
			# process left node
			if n1.left:
				queue.append((n1.left, n2.left))
			elif n2.left:  # no root1, assign root2 node to root1
				n1.left = n2.left
				n2.left = None
			
			# process right node
			if n1.right:
				queue.append((n1.right, n2.right))
			elif n2.right:  # no root1, assign root2 node to root1
				n1.right = n2.right
				n2.right = None
		
		return root1

"""
time complexity:
- O(n); n is the number of nodes in root1

space complexity:
- O(m)
"""