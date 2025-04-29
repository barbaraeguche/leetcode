# name: 2278. percentage of letter in string
# link: https://leetcode.com/problems/percentage-of-letter-in-string

# solution #
class Solution:
	def percentageLetter(self, s: str, letter: str) -> int:
		count = s.count(letter)
		
		# letter doesn't exist in string
		if count == 0:
			return 0
		
		return math.floor((count / len(s)) * 100)
	