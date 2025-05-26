# name: 973. k closest points to origin
# link: https://leetcode.com/problems/k-closest-points-to-origin

# solution #
import heapq as hq

class Solution:
	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		heap = []
		
		for point in points:
			x, y = point
			# find the distance to the origin
			dist = self.distance(x, y)
			# add to heap (min-value here becomes the distance)
			hq.heappush(heap, (dist, point))
		
		# find the closest k
		heap = hq.nsmallest(k, heap)
		return [h[1] for h in heap]
	
	@staticmethod
	def distance(x: int, y: int) -> float:
		a, b = ((x - 0) ** 2), ((y - 0) ** 2)
		return math.sqrt(a + b)
