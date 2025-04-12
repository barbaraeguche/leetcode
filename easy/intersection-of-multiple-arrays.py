# name: 2248. intersection of multiple arrays
# link: https://leetcode.com/problems/intersection-of-multiple-arrays

# solution #
class Solution:
	def intersection(self, nums: List[List[int]]) -> List[int]:
		arr = nums[0]
		
		for num in nums[1:]:
			arr = list(set(arr) & set(num))
		
		# sort the array
		arr.sort()
		
		return arr