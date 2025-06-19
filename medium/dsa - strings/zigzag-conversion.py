# name: 6. zigzag conversion
# link: https://leetcode.com/problems/zigzag-conversion

# solution #
class Solution:
	def convert(self, s: str, numRows: int) -> str:
		idx, length = 0, len(s)
		
		# for each row
		matrix = ["" for i in range(numRows)]
		
		def isStrEmpty() -> bool:
			return idx == length
		
		while idx < length:
			# top to bottom
			for i in range(0, numRows):
				if isStrEmpty():
					break
				
				matrix[i] += s[idx]
				idx += 1
			
			# bottom to top
			for i in range(numRows - 2, 0, -1):
				if isStrEmpty():
					break
				
				matrix[i] += s[idx]
				idx += 1
		
		return "".join(matrix)

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""