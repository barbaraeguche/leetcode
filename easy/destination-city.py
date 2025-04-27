# name: 1436. destination city
# link: https://leetcode.com/problems/destination-city

# solution #
class Solution:
	def destCity(self, paths: List[List[str]]) -> str:
		start = [path[0] for path in paths]
		stop = [path[1] for path in paths if path[1] not in start]
		
		return "".join(stop)
	