# name: 344. reverse string
# link: https://leetcode.com/problems/reverse-string

# solution #
class Solution:
	def reverseString(self, s: List[str]) -> None:
		"""
		Do not return anything, modify s in-place instead.
		"""
		a, b = 0, len(s) - 1
		
		while a < b:
			swap = s[a]
			s[a] = s[b]
			s[b] = swap
			
			# increment and decrement
			a += 1
			b -= 1