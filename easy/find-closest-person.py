# name: 3516. find closest person
# link: https://leetcode.com/problems/find-closest-person

# solution #
class Solution:
	def findClosest(self, x: int, y: int, z: int) -> int:
		x_z = abs(x - z)
		y_z = abs(y - z)
		
		if x_z < y_z:
			return 1
		
		if y_z < x_z:
			return 2
		
		return 0