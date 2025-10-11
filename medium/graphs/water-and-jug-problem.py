# name: 365. water and jug problem
# link: https://leetcode.com/problems/water-and-jug-problem

# solution #
class Solution:
	def canMeasureWater(self, x: int, y: int, target: int) -> bool:
		# impossible
		if target > x + y:
			return False
		
		seen, queue = set(), deque([(0, 0)])
		
		while queue:
			a, b = queue.popleft()
			
			# can reach target
			if a + b == target:
				return True
			
			# do not recompute
			if (a, b) in seen:
				continue
			seen.add((a, b))
			
			# any of point 1 and point 2
			possibilities = [(x, b), (a, y), (0, b), (a, 0)]
			
			queue.extend(possibilities)
			
			# pour into b
			water = min(a, y - b)
			queue.append((a - water, b + water))
			
			# pour into a
			water = min(b, x - a)
			queue.append((a + water, b - water))
		
		return False

"""
time complexity:
- O(x * y)

space complexity:
- O(x * y)
"""