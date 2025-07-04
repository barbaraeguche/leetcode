# name: 1268. search suggestions system
# link: https://leetcode.com/problems/search-suggestions-system

# solution #
class TrieNode:
	def __init__(self):
		self.children = {}
		self.suggestions = []
	
	def addSuggestions(self, product):
		if len(self.suggestions) < 3:
			self.suggestions.append(product)

class Solution:
	def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
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
				node.addSuggestions(prod)  # at most 3; constant space
		
		# find the top three for each search word
		suggestions, node = [], root
		
		for char in searchWord:
			if node:
				node = node.children.get(char)
			suggestions.append(node.suggestions if node else [])
		
		return suggestions

"""
time complexity:
- O((n * log(n)) + (n * m) + k); n is the number of products, m is the length of each word; k is the length of searchWord

space complexity:
- O(n * m)
"""