# name: 2706. buy two chocolates
# link: https://leetcode.com/problems/buy-two-chocolates

# solution #
import heapq as hq

class Solution:
	def buyChoco(self, prices: List[int], money: int) -> int:
		heap = []
		
		for price in prices:
			# store as max-heap to pop expensive ones
			hq.heappush(heap, -price)
			
			# keep heap with only two values
			if len(heap) > 2:
				hq.heappop(heap)
		
		# calculate the price after buying the two least expensive chocolates
		leftover_price = money - (-heap[0] + -heap[1])
		return money if leftover_price < 0 else leftover_price
