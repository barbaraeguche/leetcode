# name: 230. kth smallest element in a bst
# link: https://leetcode.com/problems/kth-smallest-element-in-a-bst

# solution #
class Solution:
	def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
		inorder = []
		
		def dfs(root: Optional[TreeNode]) -> None:
			if root:
				dfs(root.left)
				inorder.append(root.val)
				dfs(root.right)
		
		dfs(root)
		return inorder[k - 1]
	
"""
time complexity:
- O(n)

space complexity:
- O(n); for stack(custom and recursion)
"""