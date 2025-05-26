# name: 252. meeting rooms
# link: https://leetcode.com/problems/meeting-rooms

# solution #
class Solution:
	def canAttendMeetings(self, intervals: List[Interval]) -> bool:
		if len(intervals) < 2:
			return True
		
		# sort by start time
		intervals = list(sorted(intervals, key=lambda x: x.start))
		
		result = [intervals[0]]
		
		for inter in intervals[1:]:
			a, b = inter.start, inter.end
			last = result[-1]
			
			# if the start of the next interval is between the last interval (not including the end of the last interval)
			if last.start <= a < last.end:
				return False
			
			# no merging interval
			else:
				result.append(inter)
		
		return True