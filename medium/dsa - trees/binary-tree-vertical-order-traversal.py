# name: 314. binary tree vertical order traversal
# link: https://leetcode.com/problems/binary-tree-vertical-order-traversal

# solution #
class Solution:
	def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
		if not root:
			return []
		
		treeMap = defaultdict(list)
		
		# min and max cols to prevent sorting
		min_col = max_col = 0
		# to keep track of node and it's col
		queue = deque([(root, 0)])
		
		# basically a level order traversal
		while queue:
			length = len(queue)
			
			for _ in range(length):
				node, col = queue.popleft()
				# use the column value as its key
				treeMap[col].append(node.val)
				
				min_col = min(min_col, col)
				max_col = max(max_col, col)
				
				# if node has children
				if node.left:
					queue.append([node.left, col - 1])
				if node.right:
					queue.append([node.right, col + 1])
		
		return [treeMap[c] for c in range(min_col, max_col + 1)]
	