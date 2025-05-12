# name: 56. merge intervals
# link: https://leetcode.com/problems/merge-intervals

# solution #
class Solution:
	def merge(self, intervals: List[List[int]]) -> List[List[int]]:
		# first sort by start times
		intervals = list(sorted(intervals, key=lambda x: x[0]))
		
		result = [intervals[0]]
		
		for inter in intervals[1:]:
			a, b = inter
			last = result[-1]
			
			# if the start interval of the next is between the last interval
			if last[0] <= a <= last[1]:
				# if the end interval of the next is later than the last interval
				if last[1] <= b:
					last[1] = b
				else: continue # else continue as the next interval is between the last interval
			
			# no merging interval
			else:
				result.append(inter)
		
		return result
