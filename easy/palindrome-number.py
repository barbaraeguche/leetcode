# name: 9. palindrome number
# link: https://leetcode.com/problems/palindrome-number

# solution #
class Solution:
	def isPalindrome(self, x: int) -> bool:
		# can never be a palindrome
		if x < 0:
			return False
		
		first, second = x, 0
		
		while x:
			second = (second * 10) + (x % 10)
			x //= 10
		
		return first == second
	