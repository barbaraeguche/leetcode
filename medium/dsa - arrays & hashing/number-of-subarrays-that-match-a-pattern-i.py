# name: 3034. number of subarrays that match a pattern i
# link: https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i

# solution #
class Solution:
	def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
		n, m = len(nums), len(pattern)
		
		count = 0
		
		for i in range(n-m):
			check = True  # remains 0 if matches pattern
			
			for j in range(m):
				n1, n2 = nums[i+j], nums[i+j+1]
				
				# current pattern
				pat = pattern[j]
				
				# not decreasing
				if pat == -1 and n2 >= n1:
					check = False
				# not equal
				if pat == 0 and n1 != n2:
					check = False
				# not increasing
				if pat == 1 and n1 >= n2:
					check = False
			
			# matches all pattern
			count += 1 if check else 0
		
		return count

"""
time complexity:
- O(n * m); n is the length of nums and mis the length of pattern

space complexity:
- O(1)
"""