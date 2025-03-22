# name: 151. reverse words in a string
# link: https://leetcode.com/problems/reverse-words-in-a-string

# solution #
class Solution:
	def reverseWords(self, s: str) -> str:
		return " ".join(s.split()[::-1])