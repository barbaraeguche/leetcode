# name: 2194. cells in a range on an excel sheet
# link: https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet

# solution #
class Solution:
	def cellsInRange(self, s: str) -> List[str]:
		a, b = s.split(':')
		
		array = []
		
		# for each character
		for i in range(ord(a[0]), ord(b[0]) + 1, 1):
			# for each number
			for j in range(int(a[1]), int(b[1]) + 1, 1):
				array.append(f"{chr(i)}{j}")
		
		return array
	