# name: 129. sum root to leaf numbers
# link: https://leetcode.com/problems/sum-root-to-leaf-numbers

# solution #
class Solution:
	def sumNumbers(self, root: Optional[TreeNode]) -> int:
		totalSum = 0
		
		def traverse(node: Optional[TreeNode], path: int) -> None:
			if not node:
				return
			
			nonlocal totalSum
			path = path * 10 + node.val
			
			# base case: at a leaf node
			if not (node.left or node.right):
				totalSum += path
				return
			
			# dfs till leaf node
			traverse(node.left, path)
			traverse(node.right, path)
		
		traverse(root, 0)
		return totalSum

"""
time complexity:
- O(n)

space complexity:
- O(h); h is the height of the tree
"""