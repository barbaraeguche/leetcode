# name: 1394. find lucky integer in an array
# link: https://leetcode.com/problems/find-lucky-integer-in-an-array

# solution #
class Solution:
	def findLucky(self, arr: List[int]) -> int:
		maxVal, count = -1, Counter(arr)
		
		for key, val in count.items():
			if key == val:
				maxVal = max(maxVal, key)
		
		return maxVal

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""