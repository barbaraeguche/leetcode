# name: 1268. search suggestions system
# link: https://leetcode.com/problems/search-suggestions-system

# solution #
class Solution:
	def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
		class TrieNode:
			def __init__(self):
				self.children = {}
				self.suggestions = []
			
			def addSuggestions(self, product):
				if len(self.suggestions) < 3:
					self.suggestions.append(product)
		
		# root node
		root = TrieNode()
		
		# insert word into trie
		for prod in sorted(products):
			node = root
			
			for char in prod:
				if not char in node.children:
					node.children[char] = TrieNode()
				
				node = node.children[char]
				# add the prod as a suggestion for the node
				node.addSuggestions(prod)
		
		# find the top three for each search word
		suggestions, node = [], root
		
		for char in searchWord:
			if node:
				node = node.children.get(char)
			suggestions.append(node.suggestions if node else [])
		
		return suggestions
	