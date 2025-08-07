# name: 116. populating next right pointers in each node
# link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node

# solution #
class Solution:
	def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
		if not root:
			return root
		
		queue = deque([root])
		
		while queue:
			count, length = 1, len(queue)
			
			for _ in range(length):
				node = queue.popleft()
				
				if count < length:
					node.next = queue[0]
					count += 1
				
				# if node has children
				if node.left:
					queue.append(node.left)
				if node.right:
					queue.append(node.right)
		
		return root
	
"""
time complexity:
- O(n)

space complexity:
- O(n)
"""