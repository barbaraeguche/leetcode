# name: 2390. removing stars from a string
# link: https://leetcode.com/problems/removing-stars-from-a-string

# solution #
class Solution:
	def removeStars(self, s: str) -> str:
		num_stars = s.count('*')
		
		while num_stars > 0:
			idx = s.index('*')
			s = s[0:idx - 1] + s[idx + 1:]
			num_stars -= 1
		
		return s