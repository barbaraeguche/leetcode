# name: 102. binary tree level order traversal
# link: https://leetcode.com/problems/binary-tree-level-order-traversal

# solution #
class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if not root:
			return []
		
		array, temp = [], []
		queue = deque([root, '#'])
		
		while queue:
			node = queue.popleft()
			
			# delimiter to keep track of each level
			if node == '#':
				# append the current row
				array.append(temp)
				# clear the temp array that kept track of row nodes
				temp = []
				
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
