# name: 290. word pattern
# link: https://leetcode.com/problems/word-pattern

# solution #
class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:
		splitted = s.split()
		
		if len(pattern) != len(splitted):
			return False
		
		word_dict = {}
		
		for k, v in zip(pattern, splitted):
			if k in word_dict and word_dict[k] != v:
				return False
			
			elif v in word_dict.values():
				key = next((key for key, val in word_dict.items() if v == val), None)
				if key != k:
					return False
			
			word_dict |= { k: v }
			
		return True
	