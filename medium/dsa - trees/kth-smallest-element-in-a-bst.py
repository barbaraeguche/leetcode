# name: 230. kth smallest element in a bst
# link: https://leetcode.com/problems/kth-smallest-element-in-a-bst

# solution #
class Solution:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		inorder = []
		
		def traversal(root: Optional[TreeNode]) -> None:
			if root:
				traversal(root.left)
				inorder.append(root.val)
				traversal(root.right)
		
		traversal(root)
		return inorder[k - 1]
	
"""
time complexity:
- O(n)

space complexity:
- O(n); for stack(custom and recursion)
"""