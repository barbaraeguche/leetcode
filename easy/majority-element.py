# name: 169. majority element
# link: https://leetcode.com/problems/majority-element

# solution #
class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		return Counter(nums).most_common(1)[0][0]
	