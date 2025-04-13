# name: 2798. number of employees who met the target
# link: https://leetcode.com/problems/number-of-employees-who-met-the-target

# solution #
class Solution:
	def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
		count = 0
		
		for hour in hours:
			if hour >= target:
				count += 1
		
		return count