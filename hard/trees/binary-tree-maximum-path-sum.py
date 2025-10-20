# name: 124. binary tree maximum path sum
# link: https://leetcode.com/problems/binary-tree-maximum-path-sum

# solution #
class Solution:
	def maxPathSum(self, root: Optional[TreeNode]) -> int:
		maxSum = float("-inf")
		
		def dfs(node):
			nonlocal maxSum
			
			if not node:
				return 0
			
			# keep max positive
			left = max(dfs(node.left), 0)
			right = max(dfs(node.right), 0)
			
			# max at current node
			currMax = node.val + left + right
			# update global max
			maxSum = max(maxSum, currMax)
			
			# take the highest child + parent
			return node.val + max(left, right)
		
		dfs(root)
		return maxSum

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""