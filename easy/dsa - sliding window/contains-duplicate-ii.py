# name: 219. contains duplicate ii
# link: https://leetcode.com/problems/contains-duplicate-ii

# solution #
class Solution:
	def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
		# cannot be 2 unique indices
		if k == 0:
			return False
		
		length, dupMap = len(nums), {}
		
		for i in range(min(k, length)):
			# duplicate in first k elements
			if nums[i] in dupMap:
				return True
			
			dupMap[nums[i]] = i
		
		for i in range(min(k, length), length):
			# abs(i, j) == k
			if nums[i-k] == nums[i]:
				return True
			
			# abs(i, j) < k
			if nums[i] in dupMap:
				return True
			
			# remove from window
			del dupMap[nums[i-k]]
			# add to window
			dupMap[nums[i]] = i
		
		return False

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""