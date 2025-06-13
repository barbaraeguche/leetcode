# name: 3024. type of triangle
# link: https://leetcode.com/problems/type-of-triangle

# solution #
class Solution:
	def triangleType(self, nums: List[int]) -> str:
		n1, n2, n3 = nums
		
		# all three sides are equal
		if n1 == n2 == n3:
			return "equilateral"
		
		# validate triangle
		if not self.isValidTriangle(n1, n2, n3):
			return "none"
		
		# any two sides are equal
		if n1 == n2 or n2 == n3 or n1 == n3:
			return "isosceles"
		
		# all three different sides
		return "scalene"
	
	def isValidTriangle(self, n1: int, n2: int, n3: int) -> bool:
		if n1 + n2 <= n3:
			return False
		if n1 + n3 <= n2:
			return False
		if n2 + n3 <= n1:
			return False
		
		return True


"""
time complexity:
- O(1)

space complexity:
- O(1)
"""