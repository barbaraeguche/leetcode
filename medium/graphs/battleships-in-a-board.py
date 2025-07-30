# name: 419. battleships in a board
# link: https://leetcode.com/problems/battleships-in-a-board

# solution #
class Solution:
	def countBattleships(self, board: List[List[str]]) -> int:
		rows, cols = len(board), len(board[0])
		
		# battleship count
		battleships = 0
		
		def dfs(r, c):
			# within range of grid
			if (
				0 <= r < rows and
				0 <= c < cols and
				board[r][c] == "X"
			):
				board[r][c] = "."  # mark this as visited
				dfs(r-1, c)  # up
				dfs(r+1, c)  # down
				dfs(r, c-1)  # left
				dfs(r, c+1)  # right
		
		for r in range(rows):
			for c in range(cols):
				if board[r][c] == "X":  # battleship found
					dfs(r, c)
					battleships += 1
		
		return battleships
	
"""
time complexity:
- O(n * m)

space complexity:
- O(n * m)
"""