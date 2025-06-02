# name: 347. top k frequent elements
# link: https://leetcode.com/problems/top-k-frequent-elements

# solution #
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		count = Counter(nums)
		freqs = [[] * i for i in range(len(nums))]
		
		# bucket sort by frequency
		for num, frq in count.items():
			freqs[frq - 1].append(num)
		
		result = []
		
		# loop backwards till find k elements
		for i in range(len(freqs) - 1, -1, -1):
			for num in freqs[i]:
				result.append(num)
				
				if len(result) == k:
					return result
		
		return []
	