# name: 242. valid anagram
# link: https://leetcode.com/problems/valid-anagram

# solution #
class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		return Counter(s) == Counter(t)