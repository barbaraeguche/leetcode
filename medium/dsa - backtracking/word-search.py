# name: 79. word search
# link: https://leetcode.com/problems/word-search

# solution #
class Solution:
	def exist(self, board: List[List[str]], word: str) -> bool:
		rows, cols = len(board), len(board[0])
		
		def dfs(r, c, idx):
			# word check
			if idx == len(word):
				return True
			
			# boundary check
			if not (
				0 <= r < rows and
				0 <= c < cols and
				board[r][c] == word[idx]
			):
				return False
			
			# save current character; mark current grid point as visited
			char = board[r][c]
			board[r][c] = "#"
			
			# as characters are only appended when it equals the current index of the given word,
			# if `string` is the same length as `word`, then we found a match
			found = (
				dfs(r+1, c, idx+1) or
				dfs(r-1, c, idx+1) or
				dfs(r, c+1, idx+1) or
				dfs(r, c-1, idx+1)
			)
			
			# backtrack
			board[r][c] = char
			return found
		
		for r in range(rows):
			for c in range(cols):
				if dfs(r, c, 0):
					return True
		
		return False

"""
time complexity:
- O(n * m * 4 * 3^(l-1)); n is the number of rows, m is the number of cols, l is the word length

space complexity:
- O(l)
"""