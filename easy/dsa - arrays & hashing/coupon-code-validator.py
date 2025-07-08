# name: 3606. coupon code validator
# link: https://leetcode.com/problems/coupon-code-validator

# solution #
class Solution:
	def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
		pattern = re.compile(r"[A-Za-z0-9_]+")
		businessLines = { "electronics":0, "grocery":1, "pharmacy":2, "restaurant":3 }
		
		validCodes = []
		
		for i, (couponCode, business) in enumerate(zip(code, businessLine)):
			# valid coupons
			if (
				isActive[i] and
				business in businessLines and
				re.fullmatch(pattern, couponCode)
			):
				validCodes.append((business, couponCode))
		
		# sort based on the restriction
		validCodes = list(sorted(validCodes, key=lambda x: (businessLines[x[0]], x[1])))
		
		return [code for _, code in validCodes]
"""
time complexity:
- O(n * m * log(n)); n is the length of array, m is the regex matching

space complexity:
- O(n)
"""