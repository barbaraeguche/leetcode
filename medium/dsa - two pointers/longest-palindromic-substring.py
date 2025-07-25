# name: 5. longest palindromic substring
# link: https://leetcode.com/problems/longest-palindromic-substring

# solution #
class Solution:
	def longestPalindrome(self, s: str) -> str:
		begin, end = 0, len(s)
		
		def checkPalindrome(i, j):
			while i >= begin and j < end:
				if s[i] != s[j]:
					break
				
				# span out check
				i, j = i - 1, j + 1
			
			# a valid palindrome
			return s[i+1:j]
		
		# initialize longest as the first char
		subString = s[0]
		
		i, j = begin, begin + 1
		
		while j < end:
			# 2-length palindrome
			if s[i] == s[j]:
				subString = max(subString, checkPalindrome(i, j), key=len)
			
			# 3-length palindrome
			if (j + 1) < end and s[i] == s[j+1]:
				subString = max(subString, checkPalindrome(i, j+1), key=len)
			
			# continue search
			i, j = i + 1, j + 1
		
		return subString

"""
time complexity:
- O(n^2)

space complexity:
- O(1)
"""