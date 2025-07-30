# name: 80. remove duplicates from sorted array ii
# link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii

# solution #
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		idx = count = 0
		# keep track of current num
		candidate = None
		
		for num in nums:
			# maximum duplicate reached
			if candidate == num and count == 2:
				continue
			
			# different number, reset count
			if candidate != num:
				count = 0
			
			candidate = num
			# store current number
			nums[idx] = candidate
			
			# increment index and count
			idx, count = idx + 1, count + 1
		
		return idx

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""