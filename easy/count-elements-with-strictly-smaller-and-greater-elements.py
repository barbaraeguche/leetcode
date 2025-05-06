# name: 2148. count elements with strictly smaller and greater elements
# link: https://leetcode.com/problems/count-elements-with-strictly-smaller-and-greater-elements

# solution #
class Solution:
	def countElements(self, nums: List[int]) -> int:
		# find min and max
		min_num, max_num = min(nums), max(nums)
		
		# find their frequencies
		min_count, max_count = nums.count(min_num), nums.count(max_num)
		
		# find total whom have no smaller or larger
		total = max_count + min_count
		
		# find count
		count = len(nums) - total
		
		return 0 if count < 0 else count
