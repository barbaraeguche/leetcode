# name: 239. sliding window maximum
# link: https://leetcode.com/problems/sliding-window-maximum

# solution #
class Solution:
	def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
		window, queue = [], deque()
		
		for i in range(k):
			# keep maximum at first index
			while queue and nums[queue[-1]] < nums[i]:
				queue.pop()
			
			queue.append(i)
		
		# store the first maximum
		window.append(nums[queue[0]])
		
		for i in range(k, len(nums)):
			# if the current max if leaving the window
			if queue[0] == i - k:
				queue.popleft()
			
			# keep maximum at first index
			while queue and nums[queue[-1]] < nums[i]:
				queue.pop()
			
			queue.append(i)
			window.append(nums[queue[0]])
		
		return window

"""
time complexity:
- O(n)

space complexity:
- O(n)
"""