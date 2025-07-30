# name: 1343. number of sub arrays of size k and average greater than or equal to threshold
# link: https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold

# solution #
class Solution:
	def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
		count = kSum = 0
		
		# the first k sum
		for i in range(k):
			kSum += arr[i]
		
		# if valid first k
		count += 1 if kSum // k >= threshold else 0
		
		for i in range(k, len(arr)):
			# exiting the window
			kSum -= arr[i - k]
			# entering the window
			kSum += arr[i]
			
			count += 1 if kSum // k >= threshold else 0
		
		return count
	
"""
time complexity:
- O(n)

space complexity:
- O(1)
"""