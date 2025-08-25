# name: 874. walking robot simulation
# link: https://leetcode.com/problems/walking-robot-simulation

# solution #
class Solution:
	def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
		# convert to set for O(1) lookup
		obstacles = {tuple(obs) for obs in obstacles}
		
		# direction: (x, y)
		# 0: North, 1: East, 2: South, 3: West
		directions = { 0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0) }
		
		# i=index for map, dist=max distance, (x, y): current plane
		i = dist = x = y = 0
		
		def calculateDist(i, j):
			return (abs(i) ** 2) + (abs(j) ** 2)
		
		for comm in commands:
			# turn right 90 deg
			if comm == -1:
				i = (i + 1) % 4
			
			# turn left 90 deg
			elif comm == -2:
				i = (i - 1) % 4
			
			# walk
			else:
				dx, dy = directions[i]
				
				for _ in range(comm):
					nx, ny = x + dx, y + dy
					
					# if you will hit obstacle, break
					if (nx, ny) in obstacles:
						break
					
					# update current plane
					x, y = nx, ny
					dist = max(dist, calculateDist(x, y))
		
		return dist
	
"""
time complexity:
- O(m * k); m is the length of commands, k is the max number in commands

space complexity:
- O(n); n is the length of obstacles
"""