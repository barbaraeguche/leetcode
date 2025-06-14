# name: 112. path sum
# link: https://leetcode.com/problems/path-sum

# solution #
class Solution:
	def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
		pathSum = 0
		
		def pathCheck(node: Optional[TreeNode]):
			nonlocal pathSum
			if not node:
				return False
			
			pathSum += node.val
			
			# base case: path sum found and is at a leaf node
			if not (node.left or node.right) and pathSum == targetSum:
				return True
			
			# dfs till leaf node
			if pathCheck(node.left) or pathCheck(node.right):
				return True
			
			# backtrack from this node
			pathSum -= node.val
			return False
		
		return pathCheck(root)

"""
time complexity:
- O(n)

space complexity:
- O(h); h is the height of the tree
"""