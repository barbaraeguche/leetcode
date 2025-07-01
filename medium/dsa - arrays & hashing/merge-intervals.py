# name: 56. merge intervals
# link: https://leetcode.com/problems/merge-intervals

# solution #
class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		# first sort by start times
		intervals = list(sorted(intervals, key=lambda x: x[0]))
		
		result = [intervals[0]]
		
		for start, stop in intervals[1:]:
			last = result[-1]
			
			# overlapping intervals
			if last[0] <= start <= last[1]:
				# update the stop time of last interval
				if last[1] <= stop:
					last[1] = stop
			
			# non-overlapping intervals
			else:
				result.append([start, stop])
		
		return result
