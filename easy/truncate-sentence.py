# name: 1816. truncate sentence
# link: https://leetcode.com/problems/truncate-sentence

# solution #
class Solution:
	def truncateSentence(self, s: str, k: int) -> str:
		return " ".join(s.split()[:k])
	