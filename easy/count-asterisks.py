# name: 2315. count asterisks
# link: https://leetcode.com/problems/count-asterisks

# solution #
class Solution:
	def countAsterisks(self, s: str) -> int:
		hit = count = 0
		
		for char in s:
			if char == "|":
				hit = 1 if hit == 2 else hit + 1
			
			# if hit is 1, we are in a pair
			if hit != 1 and char == "*":
				count += 1
		
		return count
