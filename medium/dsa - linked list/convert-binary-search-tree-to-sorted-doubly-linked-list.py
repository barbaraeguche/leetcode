# name: 426. convert binary search tree to sorted doubly linked list
# link: https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list

# solution #
class Solution:
	def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
		# edge case
		if not root:
			return None
		
		head = curr = None
		
		# basically an inorder traversal
		def traversal(node: 'Optional[Node]'):
			if node:
				nonlocal head, curr
				traversal(node.left)
				
				# set head if not set
				if not head:
					head = Node(node.val)
					curr = head
				else:
					# add to list
					node.left, curr.right = curr, node
					curr = node
				
				traversal(node.right)
		
		# call the function
		traversal(root)
		
		# complete the cycle
		head.left, curr.right = curr, head
		
		return head

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""