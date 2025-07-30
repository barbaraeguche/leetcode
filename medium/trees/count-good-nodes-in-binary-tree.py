# name: 1448. count good nodes in binary tree
# link: https://leetcode.com/problems/count-good-nodes-in-binary-tree

# solution #
class Solution:
	def goodNodes(self, root: TreeNode) -> int:
		currMax, count = float('-inf'), 0
		
		def countGood(node: TreeNode, maxVal: int):
			if not node:
				return
			
			nonlocal count
			
			# update current max
			maxVal = max(maxVal, node.val)
			# increment count if the current max is not greater than node val
			count += 1 if maxVal <= node.val else 0
			
			# recurse
			countGood(node.left, maxVal)
			countGood(node.right, maxVal)
		
		countGood(root, currMax)
		return count

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""