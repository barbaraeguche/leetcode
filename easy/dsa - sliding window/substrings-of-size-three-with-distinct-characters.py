# name: 1876. substrings of size three with distinct characters
# link: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters

# solution #
class Solution:
	def countGoodSubstrings(self, s: str) -> int:
		count = 0
		
		for i in range(len(s) - 2):
			a, b, c = s[i], s[i+1], s[i+2]
			
			# three distinct characters
			if a != b and a != c and b != c:
				count += 1
		
		return count

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""