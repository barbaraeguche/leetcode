# name: 212. word search ii
# link: https://leetcode.com/problems/word-search-ii

# solution #
class TrieNode:
	def __init__(self):
		self.children = {}
		self.index = -1
	
	def insert(self, idx, word):
		node = self
		
		for char in word:
			if not char in node.children:
				node.children[char] = TrieNode()
			node = node.children[char]
		
		# mark the index of the word
		node.index = idx

class Solution:
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		root = TrieNode()
		
		# build the trie
		for idx, word in enumerate(words):
			root.insert(idx, word)
		
		rows, cols = len(board), len(board[0])
		foundWords = []
		
		def dfs(r, c, node):
			# boundary check
			if not (0 <= r < rows and 0 <= c < cols):
				return
			
			char = board[r][c]
			
			# invalid word
			if not char in node.children:
				return
			
			nextNode = node.children[char]
			# found a word
			if nextNode.index != -1:
				foundWords.append(words[nextNode.index])
				nextNode.index = -1  # mark as visited
			
			# mark as visited
			board[r][c] = '#'
			
			dfs(r-1, c, nextNode)
			dfs(r+1, c, nextNode)
			dfs(r, c-1, nextNode)
			dfs(r, c+1, nextNode)
			
			# backtrack
			board[r][c] = char
		
		for r in range(rows):
			for c in range(cols):
				dfs(r, c, root)
		
		return foundWords
	
"""
w * l
n * m * 4^s

time complexity:
- O(n * m * 4 * 3^(t-1)); n is the number of rows, m is the number of cols, t is the max length of any word in words

space complexity:
- O(w * l); w is the number of words, l is the average length of each word
"""