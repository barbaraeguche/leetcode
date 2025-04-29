# name: 2255. count prefixes of a given string
# link: https://leetcode.com/problems/count-prefixes-of-a-given-string

# solution #
class Solution:
	def countPrefixes(self, words: List[str], s: str) -> int:
		count, length = 0, len(s)
		
		for word in words:
			if (l := len(word)) <= length and word == s[:l]:
				count += 1
	
		return count
	