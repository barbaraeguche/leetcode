# name: 2185. counting words with a given prefix
# link: https://leetcode.com/problems/counting-words-with-a-given-prefix

# solution #
class Solution:
	def prefixCount(self, words: List[str], pref: str) -> int:
		count = 0
		
		for word in words:
			if word.startswith(pref):
				count += 1
		
		return count
