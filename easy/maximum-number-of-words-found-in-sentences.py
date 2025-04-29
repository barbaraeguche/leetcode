# name: 2114. maximum number of words found in sentences
# link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences

# solution #
class Solution:
	def mostWordsFound(self, sentences: List[str]) -> int:
		count = 0
		
		for sen in sentences:
			count = max(count, len(sen.split()))
		
		return count
