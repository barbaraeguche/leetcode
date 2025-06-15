# name: 567. permutation in string
# link: https://leetcode.com/problems/permutation-in-string

# solution #
from collections import Counter

class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		n, m = len(s1), len(s2)
		
		# cannot be a permutation
		if n > m:
			return False
		
		s1Count = Counter(s1)
		windowCount = Counter(s2[:n])
		
		# permutation in the first n characters
		if windowCount == s1Count:
			return True
		
		for i in range(n, m):
			# remove leftmost char of the window
			leftChar = s2[i - n]
			windowCount[leftChar] -= 1
			
			if windowCount[leftChar] == 0:
				del windowCount[leftChar]
			
			# add new char to the window
			rightChar = s2[i]
			windowCount[rightChar] += 1
			
			if windowCount == s1Count:
				return True
		
		return False

"""
time complexity:
- O(m)

space complexity:
- O(1)
"""