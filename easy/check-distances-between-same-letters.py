# name: 2399. check distances between same letters
# link: https://leetcode.com/problems/check-distances-between-same-letters

# solution #
class Solution:
	def checkDistances(self, s: str, distance: List[int]) -> bool:
		base = ord('a')
		
		for char in set(s):
			idx = ord(char) - base
			
			if self.indices(char, s) != distance[idx]:
				return False
		
		return True
	
	@staticmethod
	def indices(char: str, string: str) -> int:
		a = b = -1
		
		# loop through string
		for i, ch in enumerate(string):
			if char == ch:
				# find first index
				if a == -1:
					a = i
				
				# find second index
				elif b == -1:
					b = i
					break
		
		# number of chars between them
		return b - a - 1
