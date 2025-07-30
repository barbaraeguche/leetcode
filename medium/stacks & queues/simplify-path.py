# name: 71. simplify path
# link: https://leetcode.com/problems/simplify-path

# solution #
class Solution:
	def simplifyPath(self, path: str) -> str:
		validPaths = []
		
		for path in path.split("/"):
			# current directory
			if not path or path == ".":
				continue
			
			# back to the previous directory
			if path == "..":
				if validPaths:
					validPaths.pop()
			
			# valid directory
			else:
				validPaths.append(f"/{path}")
		
		# start as a valid directory
		return "".join(validPaths) if validPaths else "/"
	
"""
time complexity:
- O(n)

space complexity:
- O(n)
"""