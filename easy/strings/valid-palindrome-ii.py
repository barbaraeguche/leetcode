# name: 680. valid palindrome ii
# link: https://leetcode.com/problems/valid-palindrome-ii

# solution #
class Solution:
	def validPalindrome(self, s: str) -> bool:
		def checkPalindrome(word: str, left: int, right: int) -> bool:
			while left < right:
				if s[left] != s[right]:
					return False
				
				left, right = left + 1, right - 1
			return True
		
		left, right = 0, len(s) - 1
		
		while left < right:
			# check if at most 1 can be removed
			if s[left] != s[right]:
				return checkPalindrome(s, left + 1, right) or checkPalindrome(s, left, right - 1)
			
			left, right = left + 1, right - 1
		return True

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""