# name: 128. longest consecutive sequence
# link: https://leetcode.com/problems/longest-consecutive-sequence

# solution #
class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		numSet = set(nums)
		longest = 0
		
		for n in numSet:
			# if start of a perceived sequence
			if not (n - 1) in numSet:
				length = 1
				
				# while a sequence
				while (n + length) in numSet:
					length += 1
				
				# max of prev longest and sequence
				longest = max(longest, length)
		
		return longest
