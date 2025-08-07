# name: 22. generate parentheses
# link: https://leetcode.com/problems/generate-parentheses

# solution #
class Solution:
	def generateParenthesis(self, n: int) -> List[str]:
		parentheses = []
		
		def backtrack(openCnt: int, closeCnt: int, path: str) -> None:
			if openCnt == closeCnt == n:
				parentheses.append(path[:])
				return
			
			# must come before a closed bracket
			if openCnt < n:
				backtrack(openCnt + 1, closeCnt, f"{path}(")
			if closeCnt < openCnt:
				backtrack(openCnt, closeCnt + 1, f"{path})")
				
		backtrack(0, 0, "")
		return parentheses
