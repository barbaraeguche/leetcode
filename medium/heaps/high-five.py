# name: 1086. high five
# link: https://leetcode.com/problems/high-five

# solution #
import heapq as hq

class Solution:
	def highFive(self, items: List[List[int]]) -> List[List[int]]:
		studentMap = defaultdict(list)
		
		for ID, score in items:
			# add to heap
			hq.heappush(studentMap[ID], score)
			# keep only the top 5
			if len(studentMap[ID]) > 5:
				hq.heappop(studentMap[ID])
		
		fiveAvg = []
		
		for key, val in studentMap.items():
			fiveAvg.append([key, sum(val) // len(val)])
		
		return list(sorted(fiveAvg, key=lambda x: x[0]))
	