# name: 2303. calculate amount paid in taxes
# link: https://leetcode.com/problems/calculate-amount-paid-in-taxes

# solution #
class Solution:
	def calculateTax(self, brackets: List[List[int]], income: int) -> float:
		taxes = 0
		
		for i, (upper, percent) in enumerate(brackets):
			# cannot be taxed at higher bracket
			earned = min(income, upper)
			# calculate your dollars
			dollars = earned - (brackets[i - 1][0] if i > 0 else 0)
			
			# calculate the tax
			tax = dollars * (percent / 100)
			taxes += tax if dollars > 0 else 0
		
		return taxes

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""