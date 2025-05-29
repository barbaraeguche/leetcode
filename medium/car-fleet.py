# name: 853. car fleet
# link: https://leetcode.com/problems/car-fleet

# solution #
class Solution:
	def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
		pair = [p for p in zip(position, speed)]
		pair.sort(reverse=True)  # sort by position descending
		
		# initially, each car is on its own fleet
		fleets = len(pair)
		lead_time = (target - pair[0][0]) / pair[0][1]
		
		for i in range(1, len(pair)):
			current_time = (target - pair[i][0]) / pair[i][1]
			
			if current_time <= lead_time:
				fleets -= 1
			else:
				lead_time = current_time
		
		return fleets
