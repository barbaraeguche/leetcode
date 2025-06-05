# name: 653. two sum iv - input is a bst
# link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst

# solution #
class Solution:
	def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
		inorder = []
		
		# since the tree is a bst, run an inorder traversal for a sorted array
		def traversal(root: Optional[TreeNode]) -> None:
			if root:
				traversal(root.left)
				inorder.append(root.val)
				traversal(root.right)
		
		# traversal call
		traversal(root)
		
		# two pointers as the array is sorted
		left, right = 0, len(inorder) - 1
		
		while left < right:
			num = inorder[left] + inorder[right]
			
			if num == k:
				return True
			
			if num > k:
				right -= 1
			else:
				left += 1
		
		return False
	