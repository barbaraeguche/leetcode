# name: 2108. find first palindromic string in the array
# link: https://leetcode.com/problems/find-first-palindromic-string-in-the-array

# solution #
class Solution:
	def firstPalindrome(self, words: List[str]) -> str:
		for word in words:
			if word == word[::-1]:
				return word
		
		return ""
	