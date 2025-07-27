# name: 1768. merge strings alternately
# link: https://leetcode.com/problems/merge-strings-alternately

# solution #
class Solution:
	def mergeAlternately(self, word1: str, word2: str) -> str:
		string, l1, l2 = "", len(word1), len(word2)
		
		for i in range(max(l1, l2)):
			if i < l1:
				string += word1[i]
			if i < l2:
				string += word2[i]
		
		return string
	