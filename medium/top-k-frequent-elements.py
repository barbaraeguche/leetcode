# name: 347. top k frequent elements
# link: https://leetcode.com/problems/top-k-frequent-elements

# solution #
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		# compute k,v pairs
		counter = Counter(nums)
		# find the k most common
		common = counter.most_common(k)
		
		# return the keys
		return [k for k,_ in common]
	