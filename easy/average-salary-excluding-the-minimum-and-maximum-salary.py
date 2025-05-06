# name: 1491. average salary excluding the minimum and maximum salary
# link: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary

# solution #
class Solution:
	def average(self, salary: List[int]) -> float:
		min_sal, max_sal = min(salary), max(salary)
		return (sum(salary) - (min_sal + max_sal)) / (len(salary) - 2)
	