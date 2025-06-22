# name: 270. closest-binary-search-tree-value
# link: https://leetcode.com/problems/closest-binary-search-tree-value

# solution #
class Solution:
	def closestValue(self, root: Optional[TreeNode], target: float) -> int:
		value = root.val
		
		def traversal(node: Optional[TreeNode]) -> None:
			if not node:
				return
			
			nonlocal value
			
			# calculate the distance
			distance = abs(target - node.val)
			currDistance = abs(target - value)
			
			# update closest value if need be
			if distance == currDistance:
				value = min(value, node.val)
			elif distance < currDistance:
				value = node.val
			
			# recursively search tree
			traversal(node.left)
			traversal(node.right)
		
		traversal(root)
		return value

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""