# name: 1550. three consecutive odds
# link: https://leetcode.com/problems/three-consecutive-odds

# solution #
class Solution:
	def threeConsecutiveOdds(self, arr: List[int]) -> bool:
		count = 0
		
		for num in arr:
			# if even, reset back to zero
			if num % 2 == 0:
				count = 0
			else:
				count += 1
			
			if count == 3:
				return True
		
		return False
