# name: 2486. append characters to string to make subsequence
# link: https://leetcode.com/problems/append-characters-to-string-to-make-subsequence

# solution #
class Solution:
	def appendCharacters(self, s: str, t: str) -> int:
		i = j = 0
		
		while i < len(s):
			if s[i] == t[j]:
				j += 1
			
			# early exit; to avoid out-of-bounds
			if j == len(t):
				break
			
			i += 1
		
		return len(t) - j

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""