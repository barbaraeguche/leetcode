# name: 297. serialize and deserialize binary tree
# link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# solution #
class Codec:
	
	def serialize(self, root):
		"""Encodes a tree to a single string.
		:type root: TreeNode
		:rtype: str
		"""
		if not root:
			return ""
		
		data, queue = [], deque([root])
		
		# bfs to serialize tree
		while queue:
			node = queue.popleft()
			
			if node:
				data.append(str(node.val))
			else:
				data.append("None")
				continue
			
			queue.append(node.left)
			queue.append(node.right)
		
		return ",".join(data)
	
	def deserialize(self, data):
		"""Decodes your encoded data to tree.
		:type data: str
		:rtype: TreeNode
		"""
		if not data:
			return None
		
		idx, nodes = 0, data.split(",")
		
		# initialize root
		root = TreeNode(int(nodes[idx]))
		idx += 1
		
		# bfs to deserialize
		queue = deque([root])
		
		while queue and idx < len(nodes):
			node = queue.popleft()
			
			if nodes[idx] != "None":
				# set the left node
				left = int(nodes[idx])
				node.left = TreeNode(left)
				queue.append(node.left)
			idx += 1
			
			# # set the right node
			if nodes[idx] != "None":
				right = int(nodes[idx])
				node.right = TreeNode(right)
				queue.append(node.right)
			idx += 1
		
		return root

"""
time complexity:
- serialize: O(n);
- deserialize: O(n)

space complexity:
- serialize: O(n)
- deserialize: O(n)
"""