# name: 253. meeting rooms ii
# link: https://leetcode.com/problems/meeting-rooms-ii

# solution #
class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
		meetings = []
		
		# +1 for start; -1 for end
		for start, end in intervals:
			meetings.append((start, 1))
			meetings.append((end, -1))
		
		# sort by start-end times
		meetings.sort()
		
		# keep track of current + max overlaps
		current = maxOverlap = 0
		
		for _, blink in meetings:
			current += blink
			maxOverlap = max(maxOverlap, current)
		
		return maxOverlap

"""
time complexity:
- O(n * log(n))

space complexity:
- O(n)
"""