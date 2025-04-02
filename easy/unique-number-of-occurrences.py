# name: 1207. unique number of occurrences
# link: https://leetcode.com/problems/unique-number-of-occurrences

# solution #
class Solution:
	def uniqueOccurrences(self, arr: List[int]) -> bool:
		counter = Counter(arr)
		values = counter.values()
		
		return len(values) == len(set(values))