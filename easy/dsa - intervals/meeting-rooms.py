# name: 252. meeting rooms
# link: https://leetcode.com/problems/meeting-rooms

# solution #
class Solution:
	def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
		if len(intervals) < 2:
			return True
		
		# sort by start time
		intervals = list(sorted(intervals, key=lambda x: x[0]))
		
		result = [intervals[0]]
		
		for start, end in intervals[1:]:
			last = result[-1]
			
			# if the start of the next interval is between the last interval (not including the end of the last interval)
			if last[0] <= start < last[1]:
				return False
			
			# no merging interval
			else:
				result.append([start, end])
		
		return True
