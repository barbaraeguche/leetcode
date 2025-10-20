# name: 1087. brace expansion
# link: https://leetcode.com/problems/brace-expansion

# solution #
class Solution:
	def expand(self, s: str) -> List[str]:
		i, n = 0, len(s)
		expanded = []
		
		while i < n:
			if s[i] == "{":
				i, original = i + 1, []
				
				# get the options
				while i < n and s[i] != "}":
					if s[i].isalpha():
						original.append(s[i])
					i += 1
				
				# first expansion
				if not expanded:
					expanded = original
					i += 1
					continue
				
				# continue the expansion for prev and curr options
				temp = []
				
				for ch1 in expanded:
					for ch2 in original:
						temp.append(f"{ch1}{ch2}")
				
				# assign back to expanded
				expanded = temp
			else:
				# first char expansion
				if not expanded:
					expanded = [s[i]]
				else:
					# continue the expansion for prev options and curr character
					temp = []
					
					for ch1 in expanded:
						temp.append(f"{ch1}{s[i]}")
					
					expanded = temp
			
			# loop
			i += 1
		
		# sort by lexicographical order
		expanded.sort()
		return expanded

"""
time complexity:
- O(n * m + (k * log(k)))
n = number of strings already in expanded
m = number of options in the current original group
k = total number of strings in the final array (after all expansions)

space complexity:
- O(n * m)
"""