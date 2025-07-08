# name: 1485. clone binary tree with random pointer
# link: https://leetcode.com/problems/clone-binary-tree-with-random-pointer

# solution #
class Solution:
	def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
		treeMap = {}
		
		def dfs(node):
			if not node:
				return node
			
			# random node reference
			if node in treeMap:
				return treeMap[node]
			
			# create a clone and store in map
			newNode = NodeCopy(node.val)
			treeMap[node] = newNode
			
			# get left, right and random nodes
			newNode.left = dfs(node.left)
			newNode.right = dfs(node.right)
			newNode.random = dfs(node.random)
			
			return newNode
		
		return dfs(root) if root else None
	
"""
time complexity:
- O(h)

space complexity:
- O(n)
"""