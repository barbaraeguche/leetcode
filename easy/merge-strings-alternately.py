# name: 1768. merge strings alternately
# link: https://leetcode.com/problems/merge-strings-alternately

# solution #
class Solution:
	def mergeAlternately(self, word1: str, word2: str) -> str:
		min_word = min(word1, word2, key=len)
		max_word = word1 if min_word != word1 else word2
		
		merged = [""] * len(min_word)
		
		for i in range(len(min_word)):
			merged[i] = word1[i] + word2[i]
		
		return "".join(merged) + max_word[len(min_word):]
	