# name: 3045. count prefix and suffix pairs ii
# link: https://leetcode.com/problems/count-prefix-and-suffix-pairs-ii

# solution #
class TrieNode:
	def __init__(self):
		self.children = {}
		self.wordCnt = 0

class Solution:
	def countPrefixSuffixPairs(self, words: List[str]) -> int:
		pairCnt, root = 0, TrieNode()
		
		for word in words:
			node = root
			
			for key in zip(word, reversed(word)):
				if not key in node.children:
					node.children[key] = TrieNode()
				node = node.children[key]
				
				# count prefix-suffix pairs
				pairCnt += node.wordCnt
			
			# keep track of word occurrence
			node.wordCnt += 1
		
		return pairCnt

"""
time complexity:
- O(n * l); n is the number of words, l is the average length of words

space complexity:
- O(n * l)
"""