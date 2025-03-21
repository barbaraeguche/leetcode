# name: 414. third maximum number
# link: https://leetcode.com/problems/third-maximum-number

# solution #
class Solution:
	def thirdMax(self, nums: List[int]) -> int:
		counter_max = Counter(nums)
		counter_arr = list(sorted(
			counter_max.most_common(), key=lambda x: x[0], reverse=True
		))
		
		if len(counter_arr) >= 3:
			return counter_arr[2][0]
		
		return counter_arr[0][0]