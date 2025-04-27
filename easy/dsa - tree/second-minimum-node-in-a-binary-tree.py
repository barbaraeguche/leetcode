# name: 671. second minimum node in a binary tree
# link: https://leetcode.com/problems/second-minimum-node-in-a-binary-tree

# solution #
class Solution:
	def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
		preorder = []
		
		# traverse through the tree
		def traversal(node: Optional[TreeNode]) -> None:
			if node:
				preorder.append(node.val)
				traversal(node.left)
				traversal(node.right)
		
		# call the method
		traversal(root)
		
		# remove duplicates and sort the array
		minimum = list(set(preorder))
		minimum.sort()
		
		return -1 if len(minimum) < 2 else minimum[1]
	