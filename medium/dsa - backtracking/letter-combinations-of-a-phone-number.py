# name: 17. letter combinations of a phone number
# link: https://leetcode.com/problems/letter-combinations-of-a-phone-number

# solution #
class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		combinations = []
		
		# digit-alphabet map
		digitsMap = {
			"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
			"6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
		}
		
		def validCombination(idx: int, comb: str):
			# found a letter combination
			if len(comb) == len(digits):
				combinations.append(comb)
				return
			
			for curStr in digitsMap[digits[idx]]:
				validCombination(idx+1, comb + curStr)
		
		validCombination(0, "")
		return combinations if digits else []
	
"""
time complexity:
- O(n * 4^n)

space complexity:
- O(n)
"""