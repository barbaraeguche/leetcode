# name: 2085. count common words with one occurrence
# link: https://leetcode.com/problems/count-common-words-with-one-occurrence

# solution #
class Solution:
	def countWords(self, words1: List[str], words2: List[str]) -> int:
		count = 0
		
		for word in set(words1):
			if words1.count(word) == 1 and words2.count(word) == 1:
				count += 1
		
		return count
	