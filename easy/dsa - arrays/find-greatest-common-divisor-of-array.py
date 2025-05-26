# name: 1979. find greatest common divisor of array
# link: https://leetcode.com/problems/find-greatest-common-divisor-of-array

# solution #
class Solution:
	def findGCD(self, nums: List[int]) -> int:
		def gdc(dividend: int, divisor: int) -> int:
			while divisor != 0:
				temp = divisor
				divisor = dividend % divisor
				dividend = temp
			return dividend
		
		return gcd(max(nums), min(nums))
