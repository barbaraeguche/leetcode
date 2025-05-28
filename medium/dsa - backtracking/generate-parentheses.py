# name: 22. generate parentheses
# link: https://leetcode.com/problems/generate-parentheses

# solution #
class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		result = []
		
		def bactrack(open_count: int, close_count: int, string: str) -> None:
			if open_count == close_count == n:
				result.append(string[:])
				return
			
			# must come before a closed bracket
			if open_count < n:
				bactrack(open_count + 1, close_count, f"{string}(")
			
			if close_count < open_count:
				bactrack(open_count, close_count + 1, f"{string})")
		
		bactrack(0, 0, "")
		return result
