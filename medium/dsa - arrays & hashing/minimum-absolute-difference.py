# name: 1200. minimum absolute difference
# link: https://leetcode.com/problems/minimum-absolute-difference

# solution #
class Solution:
	def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
		arr.sort()
		
		minDiff, result = abs(arr[1] - arr[0]), []
		
		for i, num in enumerate(arr[:-1]):
			n1, n2 = arr[i], arr[i+1]
			diff = abs(n2 - n1)
			
			# new diff has been found, clear array
			if diff < minDiff:
				result.clear()
				result.append([n1, n2])
			
			# append for the same difference
			if diff == minDiff:
				result.append([n1, n2])
			
			# update diff
			minDiff = min(minDiff, diff)
		
		return result
