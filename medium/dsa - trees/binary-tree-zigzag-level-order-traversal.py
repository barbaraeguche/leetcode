# name: 103. binary tree zigzag level order traversal
# link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal

# solution #
class Solution:
	def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if not root:
			return []
		
		# keep track of level, odd levels are reversed
		idx = 0
		
		array, temp = [], []
		queue = deque([root, '#'])
		
		while queue:
			node = queue.popleft()
			
			# delimiter to keep track of each level
			if node == '#':
				temp = temp if idx % 2 == 0 else temp[::-1]
				
				# append the current row
				array.append(temp)
				# clear the temp array that kept track of row nodes
				temp = []
				# switch to either odd or even depending on previous state
				idx = 1 if idx == 0 else 0
				
				# append delimiter if not the only element remaining
				if len(queue) > 0:
					queue.append('#')
			else:
				# append the value
				temp.append(node.val)
				
				# if node has children
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
		
		return array
