# name: 938. range sum of bst
# link: https://leetcode.com/problems/range-sum-of-bst

# solution #
class Solution:
	def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
		summation = 0
		
		queue = deque([root])
		while queue:
			node = queue.popleft()
			
			if low <= node.val <= high:
				summation += node.val
			
			if node.left:
				queue.append(node.left)
			if node.right:
				queue.append(node.right)
		
		return summation
