# name: 1496. path crossing
# link: https://leetcode.com/problems/path-crossing

# solution #
class Solution:
	def isPathCrossing(self, path: str) -> bool:
		origin = (0, 0)
		seen = set()
		seen.add(origin)
		
		for p in path:
			x, y = origin
			
			if p == 'N':
				origin = (x, y+1)
			elif p == 'S':
				origin = (x, y-1)
			
			elif p == 'E':
				origin = (x+1, y)
			elif p == 'W':
				origin = (x-1, y)
			
			if origin in seen:
				return True
			
			seen.add(origin)
		
		return False