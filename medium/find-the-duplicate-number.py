# name: 287. find the duplicate number
# link: https://leetcode.com/problems/find-the-duplicate-number

# solution #
class Solution:
	def findDuplicate(self, nums: List[int]) -> int:
		counter = [k for k,v in Counter(nums).items() if v > 1]
		return counter[0]
