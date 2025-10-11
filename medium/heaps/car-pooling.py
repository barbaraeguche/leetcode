# name: 1094. car pooling
# link: https://leetcode.com/problems/car-pooling

# solution #
import heapq as hq

class Solution:
	def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
		heap = []
		
		# add all trips to the heap
		for trip in trips:
			cnt, src, dest = trip
			hq.heappush(heap, (src, dest, cnt, False))
		
		# process by pickup location
		while heap:
			src, dest, cnt, picked = hq.heappop(heap)
			
			if not picked:
				capacity -= cnt
				
				# impossible to pick and drop all
				if capacity < 0:
					return False
				
				# push to calculate drop off
				hq.heappush(heap, (dest, src, cnt, True))
			
			# dropping off; free up seats
			else:
				capacity += cnt
		
		return True

"""
time complexity:
- O(n * log(n))

space complexity:
- O(n)
"""