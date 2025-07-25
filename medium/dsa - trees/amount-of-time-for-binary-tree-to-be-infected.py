# name: 2385. amount of time for binary tree to be infected
# link: https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected

# solution #
class Solution:
	def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
		queue, adjacentList = deque([root]), defaultdict(list)
		
		# transform tree to a graph
		while queue:
			for _ in range(len(queue)):
				node = queue.popleft()
				
				# if node has children
				if node.left:
					queue.append(node.left)
					adjacentList[node.val].append(node.left.val)
					adjacentList[node.left.val].append(node.val)
				
				if node.right:
					queue.append(node.right)
					adjacentList[node.val].append(node.right.val)
					adjacentList[node.right.val].append(node.val)
		
		infected, seen = -1, set()
		
		# start from the given value
		queue.append(start)
		
		while queue:
			for _ in range(len(queue)):
				node = queue.popleft()
				
				# mark node as visited
				seen.add(node)
				
				for dest in adjacentList[node]:
					if not dest in seen:
						queue.append(dest)
			
			# keep track of time
			infected += 1
		
		return infected

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""