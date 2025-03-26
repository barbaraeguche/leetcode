# name: 2490. circular sentence
# link: https://leetcode.com/problems/circular-sentence

# solution #
class Solution:
	def isCircularSentence(self, sentence: str) -> bool:
		split = sentence.split()
		
		for i in range(len(split) - 1):
			if split[i][-1] != split[i+1][0]:
				return False
		
		return split[0][0] == split[-1][-1]