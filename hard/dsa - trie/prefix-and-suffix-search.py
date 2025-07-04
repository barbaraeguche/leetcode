# name: 745. prefix and suffix search
# link: https://leetcode.com/problems/prefix-and-suffix-search

# solution #
class TrieNode:
	def __init__(self):
		self.children = {}
		self.indices = set()

class WordFilter:
	
	def __init__(self, words: List[str]):
		self.cacheMap = {}
		self.prefRoot, self.suffRoot = TrieNode(), TrieNode()
		
		for idx, word in enumerate(words):
			preNode, sufNode = self.prefRoot, self.suffRoot
			
			for pref, suff in zip(word, reversed(word)):
				# add from prefix
				if pref not in preNode.children:
					preNode.children[pref] = TrieNode()
				preNode = preNode.children[pref]
				
				# add from suffix
				if suff not in sufNode.children:
					sufNode.children[suff] = TrieNode()
				sufNode = sufNode.children[suff]
				
				# mark the index
				preNode.indices.add(idx)
				sufNode.indices.add(idx)
	
	def f(self, pref: str, suff: str) -> int:
		preNode, sufNode = self.prefRoot, self.suffRoot
		
		# memoization
		if (pref, suff) in self.cacheMap:
			return self.cacheMap[(pref, suff)]
		
		# find prefix
		for char in pref:
			if char not in preNode.children:
				return -1
			preNode = preNode.children[char]
		
		# find suffix
		for char in reversed(suff):
			if char not in sufNode.children:
				return -1
			sufNode = sufNode.children[char]
		
		# get the matching word-index pairs
		commonIndices = preNode.indices & sufNode.indices
		
		# no pref-suff pair in trie
		if not commonIndices:
			return -1
		
		# get the index of the pair with the largest index
		largestIndex = max(commonIndices)
		
		# save previous computed pairs
		self.cacheMap[(pref, suff)] = largestIndex
		
		# return the index
		return largestIndex

"""
time complexity:
- init: O(n * l); n is the number of words, l is the average length of words
- f: O(p + s + n); p is the length of prefix query, s is the length of suffix query, n is the intersection

space complexity:
- init: O(n * l)
- f: O(q); q is the number of unique queries
"""