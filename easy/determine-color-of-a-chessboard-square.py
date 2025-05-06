# name: 1812. determine color of a chessboard square
# link: https://leetcode.com/problems/determine-color-of-a-chessboard-square

# solution #
class Solution:
	def squareIsWhite(self, coordinates: str) -> bool:
		x, y = coordinates
		
		is_x_even = (ord(x) - ord('a')) % 2 == 0
		is_y_even = int(y) % 2 == 0
		
		return (is_x_even and is_y_even) or (not (is_x_even or is_y_even))
	