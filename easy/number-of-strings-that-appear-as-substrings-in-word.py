# name: 1967. number of strings that appear as substrings in word
# link: https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word

# solution #
class Solution:
	def numOfStrings(self, patterns: List[str], word: str) -> int:
		return sum(1 for s in patterns if s in word)
	