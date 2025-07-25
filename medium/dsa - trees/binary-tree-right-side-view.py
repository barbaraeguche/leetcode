# name: 199. binary tree right side view
# link: https://leetcode.com/problems/binary-tree-right-side-view

# solution #
class Solution:
	def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
		if not root:
			return []
		
		array, queue = [], deque([root])
		
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
			
			# append the last element on this row
			# the last element is what is visible from the right side
			array.append(temp[-1])
		
		return array
