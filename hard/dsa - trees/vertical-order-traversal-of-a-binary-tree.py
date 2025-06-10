# name: 987. vertical order traversal of a binary tree
# link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree

# solution #
class Solution:
	def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
		treeMap = defaultdict(list)
		
		# min and max cols to prevent sorting
		min_col = max_col = 0
		# to keep track of node, row, and col
		queue = deque([(root, 0, 0)])
		
		# basically a level order traversal
		while queue:
			length = len(queue)
			
			for _ in range(length):
				node, row, col = queue.popleft()
				
				# use the column value as its key
				# store as (val, row) as tuple
				treeMap[col].append((node.val, row))
				
				min_col = min(min_col, col)
				max_col = max(max_col, col)
				
				# if node has children
				if node.left:
					queue.append((node.left, row + 1, col - 1))
				if node.right:
					queue.append((node.right, row + 1, col + 1))
		
		result = []
		
		# sort values by row val then by node val
		for c in range(min_col, max_col + 1):
			# to remove redundant sorting
			if len(treeMap[c]) > 1:
				treeMap[c] = sorted(treeMap[c], key=lambda x: (x[1], x[0]))
			
			# take only the node val
			result.append([val for val, row in treeMap[c]])
		
		return result
