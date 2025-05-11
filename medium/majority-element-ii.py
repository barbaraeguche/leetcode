# name: 229. majority element ii
# link: https://leetcode.com/problems/majority-element-ii

# solution #
class Solution:
	def majorityElement(self, nums: List[int]) -> List[int]:
		ref = math.floor(len(nums) / 3)
		counter = Counter(nums)
		
		return [k for k,v in counter.items() if v > ref]
	