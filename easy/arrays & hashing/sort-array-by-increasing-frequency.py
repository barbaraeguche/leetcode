# name: 1636. sort-array-by-increasing-frequency
# link: https://leetcode.com/problems/sort-array-by-increasing-frequency

# solution #
class Solution:
	def frequencySort(self, nums: List[int]) -> List[int]:
		numMap = defaultdict(int)
		
		# store frequencies in map
		for num in nums:
			numMap[num] += 1
		
		# sort frequencies
		return sorted(nums, key=lambda x: (numMap[x], -x))

"""
time complexity:
- O(n * log(n))

space complexity:
- O(n)
"""