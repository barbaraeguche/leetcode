# name: 138. copy list with random pointer
# link: https://leetcode.com/problems/copy-list-with-random-pointer

# solution #
class Solution:
	def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
		listMap = {}
		
		def traversal(node):
			if not node:
				return node
			
			# random node reference
			if node in listMap:
				return listMap[node]
			
			# create a clone and store in map
			newNode = Node(node.val)
			listMap[node] = newNode
			
			# get next and random nodes
			newNode.next = traversal(node.next)
			newNode.random = listMap.get(node.random)
			
			return newNode
		
		return traversal(head)

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""