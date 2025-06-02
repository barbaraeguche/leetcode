# name: 278. first bad version
# link: https://leetcode.com/problems/first-bad-version

# solution #
class Solution:
	def firstBadVersion(self, n: int) -> int:
		l, r = 1, n
		
		while l <= r:
			mid = (l + r) // 2
			isBad = isBadVersion(mid)
			
			if isBad:
				r = mid - 1
			else:
				l = mid + 1
		
		return l
