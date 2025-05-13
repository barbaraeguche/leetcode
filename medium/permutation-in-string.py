# name: 567. permutation in string
# link: https://leetcode.com/problems/permutation-in-string

# solution #
class Solution:
	def checkInclusion(self, s1: str, s2: str) -> bool:
		# cannot be a permutation of a string shorter than it
		if len(s1) > len(s2):
			return False
		
		length = len(s1)
		
		# keep frequency count
		counter_s1 = Counter(s1)
		
		for i in range(0, len(s2) - length + 1):
			if len(counter_s1 - Counter(s2[i:i + length])) == 0:
				return True
		
		return False
