# name: 15. 3sum
# link: https://leetcode.com/problems/3sum

# solution #
class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		triplets = set()
		
		# keep hold of each num
		# perform two-sum-ii to find other two numbers
		for i, num in enumerate(nums):
			l, r = i + 1, len(nums) - 1
			
			while l < r:
				n1, n2 = nums[l], nums[r]
				two_sum = n1 + n2
				
				# for any unique three digits that equal 0
				# the sum of any two will equal the opposite of the third
				target = -num
				
				if two_sum == target:
					triplet = tuple([n1, n2, num])
					triplets.add(triplet)
				
				if two_sum > target:
					r -= 1
				else:
					l += 1
		
		return [list(triplet) for triplet in triplets]

"""
time complexity:
- O(n^2)

space complexity:
- O(n)
"""