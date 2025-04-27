# name: 2810. faulty keyboard
# link: https://leetcode.com/problems/faulty-keyboard

# solution #
class Solution:
	def finalString(self, s: str) -> str:
		num_i = s.count('i')
		
		while num_i > 0:
			idx = s.index('i')
			s = s[:idx][::-1] + s[idx + 1:]
			num_i -= 1
		
		return s
	