# name: 103. binary tree zigzag level order traversal
# link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# solution #
class Solution:
	def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if not root:
			return []
		
		# keep track of level, odd levels are reversed
		idx = 0
		
		array = []
		queue = deque([root])
		
		while queue:
			length = len(queue)
			temp = []
			
			for _ in range(length):
				node = queue.popleft()
				# append the value
				temp.append(node.val)
				
				# if node has children
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
			
			# append the current row
			array.append(temp if idx == 0 else temp[::-1])
			# switch by row
			idx = 1 if idx == 0 else 0
		
		return array
