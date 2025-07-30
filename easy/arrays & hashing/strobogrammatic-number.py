# name: 246. strobogrammatic number
# link: https://leetcode.com/problems/strobogrammatic-number

# solution #
class Solution:
	def isStrobogrammatic(self, num: str) -> bool:
		position, stroboArr = len(num) - 1, []
		stroboMap = { "0":"0", "1":"1", "6":"9", "8":"8", "9":"6" }
		
		while position >= 0:
			number = num[position]
			
			# find the corresponding strobo number
			stroboNum = stroboMap[number] if number in stroboMap else "-1"
			# add to list
			stroboArr.append(stroboNum)
			
			# iterate back
			position -= 1
		
		return "".join(stroboArr) == num

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""