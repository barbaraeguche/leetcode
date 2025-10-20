# name: 442. find all duplicates in an array
# link: https://leetcode.com/problems/find-all-duplicates-in-an-array

# solution #
class Solution:
	def findDuplicates(self, nums: List[int]) -> List[int]:
		result = []
		
		for n in nums:
			idx = abs(n) - 1
			if nums[idx] < 0:
				result.append(abs(n))
			else:
				nums[idx] = -nums[idx]
		
		return result

"""
time complexity:
- O(n)

space complexity:
- O(k); k is the number of duplicate elements
"""