# name: 605. can place flowers
# link: https://leetcode.com/problems/can-place-flowers

# solution #
class Solution:
	def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
		# edge case: no flowers
		if n == 0:
			return True
		
		idx, length = 0, len(flowerbed)
		
		while idx < length:
			leftPot, rightPot = max(0, idx - 1), min(idx + 1, length - 1)
			
			# both adjacent beds are free
			if flowerbed[leftPot] == flowerbed[idx] == flowerbed[rightPot] == 0:
				n -= 1  # decrement flower count
				idx += 2  # move to the next non-adjacent bed
				
				# placed all flowers early
				if n == 0:
					return True
			
			# either before or after pots are filled
			# move to the next bed
			else:
				idx += 1
		
		# n == 0 if all flowers were placed
		return n == 0

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""