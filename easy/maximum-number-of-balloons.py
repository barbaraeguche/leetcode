# name: 1189. maximum number of balloons
# link: https://leetcode.com/problems/maximum-number-of-balloons

# solution #
class Solution:
	def maxNumberOfBalloons(self, text: str) -> int:
		hashm = {}
		
		for char in "balon":
			hashm |= { char: text.count(char) }
		
		# if count < 2 then don't split it
		l_count, o_count = hashm["l"], hashm["o"]
		
		if l_count < 2 or o_count < 2:
			return 0
		
		hashm["l"] = hashm["l"] // 2
		hashm["o"] = hashm["o"] // 2
		
		return min(v for k, v in hashm.items())
	