# name: 66. plus one
# link: https://leetcode.com/problems/plus-one

# solution #
class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		digits_str = ''.join(map(str, digits))
		plus_one = int(digits_str) + 1
		
		return list(map(int, str(plus_one)))
	