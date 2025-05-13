# name: 438. find all anagrams in a string
# link: https://leetcode.com/problems/find-all-anagrams-in-a-string

# solution #
class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		# cannot be a permutation of a string shorter than it
		if len(p) > len(s):
			return []
		
		length = len(p)
		result = []
		
		# keep frequency count
		counter_p = Counter(p)
		
		for i in range(0, len(s) - length + 1):
			if len(counter_p - Counter(s[i:i + length])) == 0:
				result.append(i)
		
		return result
