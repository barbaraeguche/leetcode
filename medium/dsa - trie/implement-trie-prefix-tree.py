# name: 208. implement trie prefix tree
# link: https://leetcode.com/problems/implement-trie-prefix-tree

# solution #
class TrieNode:
	def __init__(self):
		self.children = {}
		self.isEnd = False

class Trie:
	
	def __init__(self):
		self.root = TrieNode()
	
	def insert(self, word: str) -> None:
		node = self.root
		
		for char in word:
			if not char in node.children:
				node.children[char] = TrieNode()
			node = node.children[char]
		
		# mark as end of the word
		node.isEnd = True
	
	def search(self, word: str) -> bool:
		node = self.root
		
		for char in word:
			if not char in node.children:
				return False
			node = node.children[char]
		
		# check is the end of the word
		return node.isEnd
	
	def startsWith(self, prefix: str) -> bool:
		node = self.root
		
		for char in prefix:
			if not char in node.children:
				return False
			node = node.children[char]
		
		# prefix is in trie
		return True
	