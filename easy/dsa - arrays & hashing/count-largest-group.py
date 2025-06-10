# name: 1399. count largest group
# link: https://leetcode.com/problems/count-largest-group

# solution #
class Solution:
	def countLargestGroup(self, n: int) -> int:
		groupMap = {}
		
		for i in range(1, n+1):
			# set the digit summation as its key
			key = self.digitSum(i)
			groupMap[key] = groupMap.get(key, 0) + 1
		
		# get the max group size
		maxSize = max(groupMap.values())
		# return the total count
		return sum(1 for v in groupMap.values() if v == maxSize)
	
	def digitSum(self, num: int) -> int:
		total = 0
		
		while num > 0:
			total += num % 10
			num //= 10
		
		return total
