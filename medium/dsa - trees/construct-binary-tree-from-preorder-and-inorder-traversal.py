# name: 105. construct binary tree from preorder and inorder traversal
# link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# solution #
class Solution:
	def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
		# to optimise when searching for index
		inorderMap = { val: idx for idx, val in enumerate(inorder) }
		index = 0
		
		def buildTreeHelper(start: int, stop: int):
			if start > stop:
				return None
			
			nonlocal index
			
			# get value at current index
			preOrderVal = preorder[index]
			index += 1
			
			rootIdx = inorderMap[preOrderVal]
			root = TreeNode(preOrderVal)
			
			root.left = buildTreeHelper(start, rootIdx - 1)
			root.right = buildTreeHelper(rootIdx + 1, stop)
			
			return root
		
		return buildTreeHelper(0, len(preorder) - 1)

"""
time complexity:
- O(n)

space complexity:
- O(n) for recursion stack
"""