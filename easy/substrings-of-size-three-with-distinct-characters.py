# name: 1876. substrings of size three with distinct characters
# link: https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters

# solution #
class Solution:
	def countGoodSubstrings(self, s: str) -> int:
		arr = []
		
		for i in range(len(s) - 2):
			a, b, c = s[i], s[i+1], s[i+2]
			
			if a != b and a != c and b != c:
				arr.append(f"{a}{b}{c}")
		
		return len(arr)