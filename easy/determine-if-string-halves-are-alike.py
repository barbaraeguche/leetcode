# name: 1704. determine if string halves are alike
# link: https://leetcode.com/problems/determine-if-string-halves-are-alike

# solution #
class Solution:
	def halvesAreAlike(self, s: str) -> bool:
		vowels = set("aeiou")
		
		length = len(s) // 2
		a, b = s[:length], s[length:]
		
		def is_equal(word: str) -> int:
			return sum(word.count(v) for v in set(word) if v.lower() in vowels)
		
		return is_equal(a) == is_equal(b)