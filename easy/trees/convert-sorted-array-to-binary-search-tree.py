# name: 108. convert sorted array to binary search tree
# link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

# solution #
class Solution:
	def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
		def arrayHelper(i, j):
			if i > j:
				return None
			
			mid = (i + j) // 2
			num = nums[mid]
			
			root = TreeNode(num)
			root.left = arrayHelper(i, mid - 1)
			root.right = arrayHelper(mid + 1, j)
			
			return root
		
		return arrayHelper(0, len(nums) - 1)

"""
time complexity:
- O(n)

space complexity:
- O(log(n))
"""