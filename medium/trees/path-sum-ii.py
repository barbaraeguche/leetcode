# name: 113. path sum ii
# link: https://leetcode.com/problems/path-sum-ii

# solution #
class Solution:
	def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
		paths = []
		
		def validPaths(node: Optional[TreeNode], pathSum, temp):
			if not node:
				return
			
			pathSum += node.val
			temp.append(node.val)
			
			# base case: path sum found and is at a leaf node
			if not (node.left or node.right) and pathSum == targetSum:
				paths.append(temp[:])
			else:
				# dfs till leaf node
				validPaths(node.left, pathSum, temp)
				validPaths(node.right, pathSum, temp)
			
			# backtrack from this node
			temp.pop()
		
		validPaths(root, 0, [])
		return paths
	
"""
time complexity:
- O(n)

space complexity:
- O(n)
"""