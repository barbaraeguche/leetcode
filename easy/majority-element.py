# name: 169. majority element
# link: https://leetcode.com/problems/majority-element

# solution #
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		"""this is the Boyer-Moore voting algorithm"""
		
		count, candidate = 0, None
		
		for num in nums:
			if count == 0:
				candidate = num
			
			count += 1 if candidate == num else -1
		
		return candidate

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""