# name: 107. binary tree level order traversal ii
# link: https://leetcode.com/problems/binary-tree-level-order-traversal-ii

# solution #
class Solution:
	def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
		# edge case
		if not root:
			return []
		
		order, queue = deque(), deque([root])
		
		while queue:
			length = len(queue)
			temp = []
			
			# for current row
			for _ in range(length):
				node = queue.popleft()
				temp.append(node.val)
				
				# if node has children
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
			
			# in reverse order
			order.appendleft(temp)
		
		return list(order)

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""