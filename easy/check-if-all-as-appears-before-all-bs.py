# name: 2124. check if all a's appears before all b's
# link: https://leetcode.com/problems/check-if-all-as-appears-before-all-bs

# solution #
class Solution:
	def checkString(self, s: str) -> bool:
		a = 'a' * s.count('a')
		b = 'b' * s.count('b')
		
		return (a + b) == s
	