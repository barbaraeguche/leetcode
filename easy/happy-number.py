# name: 202. happy number
# link: https://leetcode.com/problems/happy-number

# solution #
class Solution:
	def isHappy(self, n: int) -> bool:
		seen = set()
		
		while n != 1:
			string = str(n)
			
			# calculate its sum of squares
			n = sum(int(num) ** 2 for num in string)
			
			# if happy
			if n == 1:
				return True
			
			# if previously computed
			if n in seen:
				return False
			else:
				# add the summation value to set
				seen.add(n)
		
		# if n == 1 already
		return True
