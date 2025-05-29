# name: 102. binary tree level order traversal
# link: https://leetcode.com/problems/binary-tree-level-order-traversal

# solution #
class Solution:
	def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if not root:
			return []
	
		array = []
		queue = deque([root])
		
		while queue:
			length = len(queue)
			temp = []
			
			# for each node in the row
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
			array.append(temp)
		
		return array
