# name: 36. valid sudoku
# link: https://leetcode.com/problems/valid-sudoku

# solution #
class Solution:
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		# row check
		for i in range(9):
			seen = set()
			for j in range(9):
				if (num := board[i][j]).isdigit():
					if num in seen:
						return False
					seen.add(num)
		
		# column check
		for i in range(9):
			seen = set()
			for j in range(9):
				if (num := board[j][i]).isdigit():
					if num in seen:
						return False
					seen.add(num)
		
		# square check
		for i in range(9):
			seen = set()
			for j in range(3):
				for k in range(3):
					r = (i // 3) * 3 + j
					c = (i % 3) * 3 + k
					
					if (num := board[r][c]).isdigit():
						if num in seen:
							return False
						seen.add(num)
		
		return True
