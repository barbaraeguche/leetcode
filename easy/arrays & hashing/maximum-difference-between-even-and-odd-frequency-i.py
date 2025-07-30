# name: 3442. maximum difference between even and odd frequency i
# link: https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i

# solution #
class Solution:
	def maxDifference(self, s: str) -> int:
		count = Counter(s)
		
		maxOdd, minEven = float('-inf'), float('inf')
		
		for freq in count.values():
			if freq % 2:
				maxOdd = max(maxOdd, freq)
			else:
				minEven = min(minEven, freq)
		
		return maxOdd - minEven

"""
time complexity:
- O(n)

space complexity:
- O(1)
"""