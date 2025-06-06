# name: 1570. dot product of two sparse vectors
# link: https://leetcode.com/problems/dot-product-of-two-sparse-vectors

# solution #
class SparseVector:
	def __init__(self, nums: List[int]):
		self.nums = nums
	
	# Return the dotProduct of two sparse vectors
	def dotProduct(self, vec: 'SparseVector') -> int:
		product = 0
		
		for a, b in zip(self.nums, vec.nums):
			if a == 0 or b == 0:
				continue
			product += (a * b)
		
		return product
