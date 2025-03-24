# name: 17. letter combinations of a phone number
# link: https://leetcode.com/problems/letter-combinations-of-a-phone-number

# solution #
class Solution:
	def letterCombinations(self, digits: str) -> List[str]:
		alphanum: Dict[int, str] = {
			"2": "abc", "3": "def",
			"4": "ghi",  "5": "jkl", "6": "mno",
			"7": "pqrs", "8": "tuv", "9": "wxyz"
		}
		
		values = [alphanum[d] for d in digits if d in alphanum]
		
		if not len(values):
			return []
		
		return ["".join(pair) for pair in product(*values)]