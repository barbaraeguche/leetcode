# name: 863. all nodes distance k in binary tree
# link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree

# solution #
class Solution:
	def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
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
		
		nodes, seen = [], set()
		
		# start from the given value
		queue.append(target.val)
		
		while queue:
			for _ in range(len(queue)):
				node = queue.popleft()
				
				# reached our target nodes
				if k == 0:
					nodes.append(node)
				
				# mark node as visited
				seen.add(node)
				
				for dest in adjacentList[node]:
					if not dest in seen:
						queue.append(dest)
			
			# early exit
			if k == 0:
				break
			
			# k-th distance is when k == 0
			k -= 1
		
		return nodes

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""