# name: 642. design search autocomplete system
# link: https://leetcode.com/problems/design-search-autocomplete-system

# solution #
class TrieNode:
	def __init__(self):
		self.children = {}
		self.words = set()
	
	def insert(self, word: str):
		node = self
		
		for char in word:
			if char not in node.children:
				node.children[char] = TrieNode()
			node = node.children[char]
			
			# keep track of prefix words
			node.words.add(word)
	
	def search(self, word: str):
		node = self
		
		for char in word:
			if char not in node.children:
				return []  # cannot be a prefix if not a children
			node = node.children[char]
		
		return node.words

class AutocompleteSystem:
	
	def __init__(self, sentences: List[str], times: List[int]):
		self.sentence = ""
		
		self.root = TrieNode()
		self.histMap = defaultdict(int)  # keep track of sentence occurrence
		
		for freq, sentence in zip(times, sentences):
			self.root.insert(sentence)
			self.histMap[sentence] = freq
	
	def input(self, c: str) -> List[str]:
		if c == "#":
			# store finished sentence
			self.root.insert(self.sentence)
			self.histMap[self.sentence] += 1
			
			self.sentence = ""  # refresh string
			return []
		
		self.sentence += c
		
		# search for words that sentence is a prefix of
		autocomplete = self.root.search(self.sentence)
		# sort by frequency, then by order, return the first three
		autocomplete = sorted(autocomplete, key=lambda x: (-self.histMap[x], x))[:3]
		
		return autocomplete

"""
time complexity:
- insert: O(l); l is the length of sentence being inserted
- search: O(p); p is the length of the prefix

- init: O(n * l); n is the length of sentences
- input: O(p + w * log(w)); w is the number of sentences in the set

space complexity:
- insert: O(l)
- search: O(w)

- init: O(n * l)
- input: O(w)
"""