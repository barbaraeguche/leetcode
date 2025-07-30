# name: 211. design add and search words data structure
# link: https://leetcode.com/problems/design-add-and-search-words-data-structure

# solution #
class TrieNode:
	def __init__(self):
		self.children = {}
		self.isEnd = False

class WordDictionary:
	
	def __init__(self):
		self.root = TrieNode()
	
	def addWord(self, word: str) -> None:
		node = self.root
		
		for char in word:
			if not char in node.children:
				node.children[char] = TrieNode()
			node = node.children[char]
		
		# mark as the end of word
		node.isEnd = True
	
	def search(self, word: str) -> bool:
		def dfs(index, node: TrieNode) -> bool:
			if index == len(word):
				return node.isEnd
			
			char = word[index]
			
			if char == ".":
				for child in node.children.values():
					if dfs(index + 1, child):
						return True
				return False
			else:
				if not char in node.children:
					return False
				return dfs(index + 1, node.children[char])
			
		return dfs(0, self.root)

"""
time complexity:
- addWord: O(n)
- search:
	- best: O(m)
	- worst (with '.'): O(b^m), where b is the branching factor (max 26)

space complexity:
- O((n * w) + m); n is the number of words, w is the length of each word, m is the recursion stack
"""