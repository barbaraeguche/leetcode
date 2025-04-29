# name: 1629. slowest key
# link: https://leetcode.com/problems/slowest-key

# solution #
class Solution:
	def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
		hashm = {}
		
		for i, time in enumerate(releaseTimes):
			char = keysPressed[i]
			
			if i == 0:
				hashm |= { char: time }
			
			else:
				diff = releaseTimes[i] - releaseTimes[i - 1]
				
				if char in hashm:
					diff = max(hashm[char], diff)
				
				hashm |= { char: diff }
		
		# find the max time diff
		max_time = max(hashm.values())
		
		# get the keys whose values equal the max time
		array = [k for k,v in hashm.items() if v == max_time]
		
		# sort the array
		array.sort()
		
		return array[-1]
	