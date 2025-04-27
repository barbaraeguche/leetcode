# name: 2000. reverse prefix of word
# link: https://leetcode.com/problems/reverse-prefix-of-word

# solution #
class Solution:
	def reversePrefix(self, word: str, ch: str) -> str:
		try:
			idx = word.index(ch) + 1
			return word[:idx][::-1] + word[idx:]
		except ValueError:
			return word
		
		return word
	