# name: 16. 3sum closest
# link: https://leetcode.com/problems/3sum-closest

# solution #
class Solution:
	def threeSumClosest(self, nums: List[int], target: int) -> int:
		# sort the array
		nums.sort()
		closest = float('inf')
		
		# keep hold of each num
		# perform two-sum-ii to find other two numbers
		for i, num in enumerate(nums):
			left, right = i + 1, len(nums) - 1
			
			while left < right:
				n1, n2 = nums[left], nums[right]
				summation = num + n1 + n2
				
				# perfect sum found
				if summation == target:
					return summation
				
				# closest is the min of summation or infinity
				if abs(target - summation) < abs(target - closest):
					closest = summation
				
				if summation < target:
					left += 1
				else:
					right -= 1
		
		return closest

"""
time complexity:
- O(n^2)

space complexity:
- O(n)
"""