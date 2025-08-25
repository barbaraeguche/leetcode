# name: 743. network delay time
# link: https://leetcode.com/problems/network-delay-time

# solution #
import heapq as hq

class Solution:
	def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
		adjacency = defaultdict(list)
		
		# build an adjacency list
		for u, v, t in times:
			adjacency[u].append((t, v))
		
		timeMap, minheap = {}, [(0, k)]
		
		while minheap:
			t, u = hq.heappop(minheap)
			
			# found a shorter time
			if u in timeMap:
				continue
			
			# mark the shortest path
			timeMap[u] = t
			
			for time, dest in adjacency[u]:
				if not dest in timeMap:
					hq.heappush(minheap, (t + time, dest))
		
		minTime = float("-inf")
		
		for i in range(1, n + 1):
			if not i in timeMap:
				return -1
			minTime = max(minTime, timeMap[i])
		
		return minTime
	
"""
time complexity:
- O(e * log(v)); v is the number of vertices and e is the number of edges

space complexity:
- O(v + e)
"""