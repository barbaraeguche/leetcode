# name: 13. roman to integer
# link: https://leetcode.com/problems/roman-to-integer

# solution #
class Solution:
	def romanToInt(self, s: str) -> int:
		integer, length = 0, len(s)
		
		symbolMap = {
			"I": 1, "V": 5, "X": 10, "L": 50,
			"C": 100, "D": 500, "M": 1000
		}
		
		def subtractNum(idx, currChar, char1, char2):
			return (
				s[idx] == currChar and
				s[idx + 1] in (char1, char2)
			)
		
		for i in range(len(s) - 1, -1, -1):
			char = s[i]
			# avoid out-of-bounds
			isInBounds = i + 1 < length
			
			if (
				isInBounds and (
					subtractNum(i, "I", "V", "X") or
					subtractNum(i, "X", "L", "C") or
					subtractNum(i, "C", "D", "M")
				)
			):
				integer -= symbolMap[char]
			
			else:
				integer += symbolMap[char]
		
		return integer

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""